CREATE TABLE IF NOT EXISTS produtos (
  id_prod integer primary key,
  nome_prod text not null,
  desc_prod text not null,
  preco_prod real not null,
  img_prod text not null
);
