import pandas as pd
import numpy as np

def load_listings(path: str) -> pd.DataFrame:
    """Carga el CSV de listings y devuelve un DataFrame."""
    return pd.read_csv(path)

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza general del dataset: precios, fechas, tipos numéricos."""
    if 'price' in df.columns:
        df['price'] = (
            df['price']
            .astype(str)
            .str.replace(r'[\$,€]', '', regex=True)
            .str.replace(',', '', regex=False)
            .astype(float)
        )
    if 'last_review' in df.columns:
        df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
    return df

def clean_neighbourhoods(df: pd.DataFrame, col: str = 'neighbourhood_cleansed') -> pd.DataFrame:
    """Normaliza nombres de barrios (quita 'Barcelona', espacios, acentos)."""
    import unicodedata
    def normalize(s):
        if not isinstance(s, str): return s
        s = s.strip().replace('Barcelona', '').strip()
        s = ''.join(c for c in unicodedata.normalize('NFD', s)
                    if unicodedata.category(c) != 'Mn')  # quitar acentos
        return s.title()
    df[col] = df[col].apply(normalize)
    df[col] = df[col].replace('', np.nan)
    return df

def top_neighbourhoods(df: pd.DataFrame, neigh_col='neighbourhood_cleansed',
                       min_listings=10, top_n=20) -> pd.DataFrame:
    """Devuelve los barrios con mayor precio medio."""
    if neigh_col not in df.columns:
        return pd.DataFrame()
    stats = (
        df.groupby(neigh_col)
        .agg(mean_price=('price', 'mean'),
             median_price=('price', 'median'),
             count=('price', 'count'))
        .query(f'count >= {min_listings}')
        .sort_values('mean_price', ascending=False)
        .head(top_n)
    )
    return stats.reset_index()