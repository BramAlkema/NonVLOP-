import psycopg2
from tqdm import tqdm
import time

#adds a bunch of fakeusers to the mastodon database

conn = psycopg2.connect(host="localhost",
                    database="mastodon_production",
                    user="mastodon", password='')
conn.autocommit = True

#ALTER DATABASE mastodon_production SET faker.locales = 'az_AZ, cs_CZ, da_DK, de_AT, de_CH, de_DE, el_GR, en_AU, en_CA, en_GB, en_IE, en_IN, en_NZ, en_PH, en_US, es_CO, es_ES, es_MX, fa_IR, fi_FI, fil_PH, fr_CH, fr_FR, he_IL, hi_IN, hr_HR, hu_HU, hy_AM, id_ID, it_IT, ka_GE, ko_KR, ne_NP, nl_BE, nl_NL, no_NO, pl_PL, pt_BR, pt_PT, ro_RO, ru_RU, sk_SK, sl_SI, sv_SE, ta_IN, th_TH, tl_PH, uk_UA, zh_CN, zh_TW;
#ON CONFLICT DO NOTHING

for i in tqdm(range(4000)):
    cursor = conn.cursor()
    try:
        cursor.execute("do $$ \
        begin \
        for r in 1..10000 loop \
        WITH new_user as ( \
          INSERT INTO accounts (username, public_key, created_at, updated_at, note, display_name) \
          VALUES ( gen_random_uuid(), 1, '2003-01-01', '2003-01-01', 'TXT', faker.name()) \
          RETURNING id AS account_ID \
        ) \
        INSERT INTO users (email, account_id, created_at, updated_at,  confirmed_at) \
        VALUES ( gen_random_uuid(), (select account_ID from new_user), '2003-01-01', '2003-01-01','2003-01-01'); \
        end loop; \
        end; \
        $$;")
    except Exception as error:
        pass
    cursor.close()
    #print(i)
