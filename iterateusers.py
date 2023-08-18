from mastodon import Mastodon
import psycopg2
from datetime import datetime
from faker import Faker

fake = Faker(['az_AZ', 'cs_CZ', 'da_DK', 'de_AT', 'de_CH', 'de_DE', 'el_GR', 'en_AU', 'en_CA', 'en_GB', 'en_IE', 'en_IN', 'en_NZ', 'en_PH', 'en_US', 'es_CO', 'es_ES', 'es_MX', 'fa_IR', 'fi_FI', 'fil_PH', 'fr_CH', 'fr_FR', 'he_IL', 'hi_IN', 'hr_HR', 'hu_HU', 'hy_AM', 'id_ID', 'it_IT', 'ja_JP', 'ka_GE', 'ko_KR', 'ne_NP', 'nl_BE', 'nl_NL', 'no_NO', 'pl_PL', 'pt_BR', 'pt_PT', 'ro_RO', 'ru_RU', 'sk_SK', 'sl_SI', 'sv_SE', 'ta_IN', 'th_TH', 'tl_PH', 'uk_UA', 'zh_CN', 'zh_TW'], use_weighting=False)

#mastodon = Mastodon(
#    client_id = 'pytooter_clientcred.secret',
#    api_base_url = 'https://mastodon.xn--sft219bi3tzwd.com'
#)

#mastodon.log_in(
#    'bram@xn--sft219bi3tzwd.com',
#    'tye-enx8tgm5GZA5vhm',
#    to_file = 'pytooter_usercred.secret'
#)

mastodon = Mastodon(
    access_token = 'pytooter_usercred.secret',
    api_base_url = 'https://mastodon.xn--sft219bi3tzwd.com'
)

#print(mastodon.search('harry*'))
#print(mastodon.account('107928996573424951'))

#mastodon.update_credentials()


conn = psycopg2.connect(host="192.168.1.50", database="mastodon_production", user="mastodon", password='NFd2Un1pi7mVD4SjXjkFY3wusLoGP8')
conn.autocommit = True
cursor = conn.cursor()
#cursor.execute("UPDATE users SET confirmed_at = %s where email = %s ;",(str(datetime.now()),'popoviczvonko@example.org',),)

#conn.commit()

#conn.close()


#sql = "select id, account_id from statuses limit 10;"
#sql = "select * from accounts limit 2;"
#sql= "select id,email from users order by id limit 3;"

cursor.execute("select account_id from users where email = %s;", ('popoviczvonko@example.org',))
#it's a tuple I reckon
id_result = cursor.fetchone()[0]
print(id_result)
cursor.execute("UPDATE accounts SET note = %s, display_name = %s where id = %s ;",
(fake.text(),fake.name(),id_result,)
,)
#cursor.execute("select private_key from accounts where id = %s;", (id_result,))
#cursor.execute(
#        "insert into statuses (text, created_at, updated_at, account_id) values (%s,%s,%s,%s);",
#            ("Test",
#            str(datetime.now()),
#            str(datetime.now()),
#            '107919496499608303'),
#)

try:
    for result in cursor.fetchall()[0]:
        print(result)
except Exception as e:
    print('None')
        # print(str(e))
conn.close()


#cursor.execute(
#        "insert into statuses (text, created_at, updated_at, account_id) values (%s,%s,%s,%s);",
#            ("Test",
#            str(datetime.now()),
#            str(datetime.now()),
#            '107919496499608303'),
#)


# user table structure
# id | email | account_id | created_at| updated_at| encrypted_password| reset_password_token |
# reset_password_sent_at |    remember_created_at     | sign_in_count |     current_sign_in_at     |
# last_sign_in_at       | current_sign_in_ip | last_sign_in_ip | admin |  confirmation_token
#|confirmed_at| confirmation_sent_at |  unconfirmed_email | locale | encrypted_otp_secret |
# encrypted_otp_secret_iv | encrypted_otp_secret_salt | consumed_timestep | otp_required_for_login |
# last_emailed_at | otp_backup_codes

# accounts table
#    "username", default: "", null: false
#     t.string "domain"
#     t.text "private_key"
#     t.text "public_key", default: "", null: false
#     t.datetime "created_at", null: false
#     t.datetime "updated_at", null: false
#     t.text "note", default: "", null: false
#     t.string "display_name", default: "", null: false
#     t.string "uri", default: "", null: false
#     t.string "url"
#     t.string "avatar_file_name"
#     t.string "avatar_content_type"
#     t.integer "avatar_file_size"
#     t.datetime "avatar_updated_at"
#     t.string "header_file_name"
#     t.string "header_content_type"
#     t.integer "header_file_size"
#     t.datetime "header_updated_at"
#     t.string "avatar_remote_url"
#     t.boolean "locked", default: false, null: false
#     t.string "header_remote_url", default: "", null: false
#     t.datetime "last_webfingered_at"
#     t.string "inbox_url", default: "", null: false
#     t.string "outbox_url", default: "", null: false
#     t.string "shared_inbox_url", default: "", null: false
#     t.string "followers_url", default: "", null: false
#     t.integer "protocol", default: 0, null: false
#     t.boolean "memorial", default: false, null: false
#     t.bigint "moved_to_account_id"
#     t.string "featured_collection_url"
#     t.jsonb "fields"
#     t.string "actor_type"
#     t.boolean "discoverable"
#     t.string "also_known_as", array: true
#     t.datetime "silenced_at"
#     t.datetime "suspended_at"
#     t.boolean "hide_collections"
#     t.integer "avatar_storage_schema_version"
#     t.integer "header_storage_schema_version"
#     t.string "devices_url"
#     t.integer "suspension_origin"
#     t.datetime "sensitized_at"
#     t.boolean "trendable"
#     t.datetime "reviewed_at"
#     t.datetime "requested_review_at"
