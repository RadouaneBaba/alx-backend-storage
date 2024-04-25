-- ranks country origins based on number of fans
SELECT origin, fans AS nb_fans FROM metal_bands ORDER BY nb_fans DESC;
