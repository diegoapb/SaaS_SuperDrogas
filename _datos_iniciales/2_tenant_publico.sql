-- Produccion

INSERT INTO "clientes_cliente" ("schema_name", "nombre") VALUES ('public', 'public');
INSERT INTO "clientes_dominio" ("domain", "is_primary", "tenant_id") VALUES ('superdrug.tk', true, 1);


-- INSERT INTO "clientes_dominio" ("domain", "is_primary", "tenant_id") VALUES ('3.13.232.82', true, 1);
-- UPDATE clientes_dominio SET domain = 'tenant.3.13.232.82' where id = 5;

-- UPDATE clientes_cliente SET schema_name = 'tenant' where id = 5;