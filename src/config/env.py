from envparse import env

######################################################################
# POSTGRESQL

POSTGRESQL_HOST = env.str('POSTGRESQL_HOST')

POSTGRESQL_PORT = env.str('POSTGRESQL_PORT')

POSTGRESQL_DBNAME = env.str('POSTGRESQL_DBNAME')

DB_USER = env.str('DB_USER')

DB_PASS = env.str('DB_PASS')
