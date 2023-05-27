from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Configuração do banco de dados
DATABASE_URL = "postgresql://user:password@localhost:5432/adventureworks"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição da entidade Produto
class Product(Base):
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    color = Column(String)
    list_price = Column(Float)

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar um novo produto
@app.post("/products/")
def create_product(product: Product):
    db = SessionLocal()
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Get em todos os produtos
@app.get("/products/")
def get_all_products():
    db = SessionLocal()
    products = db.query(Product).all()
    return products

# Função Ler
@app.get("/products/{product_id}")
def get_product(product_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

# Função atualizar
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    db = SessionLocal()
    existing_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    existing_product.name = product.name
    existing_product.color = product.color
    existing_product.list_price = product.list_price
    db.commit()
    return {"message": "Produto atualizado com sucesso"}

# Função delete
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    db = SessionLocal()
    existing_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(existing_product)
    db.commit()
    return {"message": "Produto removido com sucesso"}

#parte 2
client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={
        "name": "Product 1",
        "color": "Red",
        "list_price": 10.99
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Product 1"

def test_get_all_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Product 1"

def test_update_product():
    response = client.put("/products/1", json={
        "name": "Updated Product",
        "color": "Blue",
        "list_price": 19.99
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Produto atualizado com sucesso"

def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Produto removido com sucesso"


# Execução da API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
