from decouple import config
from supabase import create_client, Client

url = config("SUPABASE_URL")
key = config("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# Registro de usuario
email = "maicol2blea@gmail.com"
password = "maicolstiven123"
user = supabase.auth.sign_in({"email": email, "password": password})

access_token = user.get("access_token")

