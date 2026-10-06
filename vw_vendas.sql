-- View: public.vw_vendas_completa

-- DROP VIEW public.vw_vendas_completa;

CREATE OR REPLACE VIEW public.vw_vendas_completa
 AS
 SELECT p.order_id,
    p.customer_id,
    c.customer_state AS uf_cliente,
    c.customer_city AS cidade_cliente,
    i.product_id,
    prod.product_category_name AS categoria_produto,
    p.data_compra,
    p.data_entrega_cliente,
    i.valor_produto,
    i.valor_frete,
    i.valor_produto + i.valor_frete AS valor_total_pedido
   FROM vw_pedidos_limpos p
     LEFT JOIN vw_itens_pedidos i ON p.order_id = i.order_id
     LEFT JOIN customers c ON p.customer_id = c.customer_id
     LEFT JOIN products prod ON i.product_id = prod.product_id;

ALTER TABLE public.vw_vendas_completa
    OWNER TO postgres;

