from cryptography.fernet import Fernet

# Храним ключ в переменной среды или .env
SECRET_KEY = Fernet.generate_key()
fernet = Fernet(SECRET_KEY)

def encrypt_text(text: str) -> str:
    return fernet.encrypt(text.encode()).decode()

def decrypt_text(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
