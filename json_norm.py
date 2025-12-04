import json
import pandas as pd

def normalize_json():
    # 1) carregar JSON (lista de visitas)
    with open("resposta.json", "r", encoding="utf-8") as f:
        visits = json.load(f)

    # 2) "desnormalizar" actionDetails para linhas, trazendo alguns campos do nível superior
    #    errors='ignore' evita falha se alguma chave meta faltar em algum registro
    df_actions = pd.json_normalize(
        visits,
        record_path="actionDetails",
        meta=["idVisit", "visitIp", "visitorId", "country"],
        errors="ignore"
    )

    # 3) filtrar apenas os actionDetails com type == "download" (tratando casos de None e maiúsc/minúsc)
    mask = df_actions["type"].astype(str).str.lower() == "download"
    df_downloads = df_actions[mask].copy()

    # 4) simplificar a coluna 'url' para apenas o nome do arquivo
    df_downloads["url"] = df_downloads["url"].apply(lambda x: x.split('/')[-1] if isinstance(x, str) else None)

    # 5) selecionar colunas desejadas
    cols = ["idVisit", "visitIp", "visitorId", "url", "serverTimePretty", "country"]
    cols_exist = [c for c in cols if c in df_downloads.columns]
    result = df_downloads[cols_exist].reset_index(drop=True)
    result.index.name = "index"

    # 6) visualizar resultado
    print(result.head())

if __name__ == '__main__':
    normalize_json()

