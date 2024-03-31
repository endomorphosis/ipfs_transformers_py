import * as huggingface_scraper from './huggingface_scraper/main.js';

let local_model_path = ""
let collection_path = ""

let s3_bucket = ""
let s3_secret_key = ""
let s3_access_key = ""
let s3_endpoint = ""
let s3_host_bucket = ""

let hf_account_name = ""
let hf_user_key = ""
let hf_org_key = ""
let hf_org_name = ""

let mysql_host = ""
let mysql_user = ""
let mysql_password = ""
let mysql_database = ""

let mysql_creds = {
    "host": mysql_host,
    "user": mysql_user,
    "password": mysql_password,
    "database": mysql_database
}

let s3_creds = {
    "accessKey": s3_access_key,
    "secretKey": s3_secret_key,
    "endpoint": s3_endpoint,
    "bucket": s3_bucket,
    "hostBucket": s3_host_bucket
}

let hf_creds = {
    "account_name": hf_account_name,
    "user_key": hf_user_key,
    "org_key": hf_org_key,
    "org_name": hf_org_name
}

process.env.mysql_creds = JSON.stringify(mysql_creds)
process.env.s3_creds = JSON.stringify(s3_creds)
process.env.hf_creds = JSON.stringify(hf_creds)
process.env.local_model_path = local_model_path
process.env.collection_path = collection_path

const scraper = new huggingface_scraper.Scraper(
    s3_creds = s3_creds,
    hf_creds = hf_creds,
    mysql_creds = mysql_creds,
    local_model_path = local_model_path,
    collection_path = collection_path
);

scraper.main();