from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
from pydantic import BaseModel
import numpy as np
from fastapi.responses import ORJSONResponse

#FUNCIONALIDADE PRINCIPAL DA APLICAÇÃO IMPLEMENTADA POR Inácio Oliveira
SECRET_KEY = "minha_chave_super_secreta"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#scopos da API sheets e drive
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

client = gspread.authorize(creds)

app = FastAPI()

def verificar_token(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=403, detail="Token inválido")
    
#comparativo dos arquivos no google sheets
class CompareRequest(BaseModel):
    sefaz: str
    sistema : str
@app.post("/comparar")
def comparar(request: CompareRequest, token: str = Depends(verificar_token)):
    try:
        df1 = pd.DataFrame(client.open(request.sefaz).sheet1.get_all_records())
        df2 = pd.DataFrame(client.open(request.sistema).sheet1.get_all_records())
        if "chave" not in df1.columns or "chave" not in df2.columns:
            raise HTTPException(status_code=400, detail="Coluna 'chave' não encontrada")
        resultado = df1.merge(df2, on="chave", how="left", indicator=True)
        diff = resultado[resultado['_merge'] == 'left_only'].drop(columns=['_merge'])
        sanitized_data = diff.replace([np.nan, np.inf, -np.inf], "").astype(str).to_dict(orient="records")
        return ORJSONResponse(content={"diferença": sanitized_data})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    