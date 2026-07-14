from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ==========================
# Chat History
# ==========================

def save_chat(user_id, role, message):

    supabase.table("chat_history").insert(
        {
            "user_id": user_id,
            "role": role,
            "message": message
        }
    ).execute()


def load_chat(user_id):

    result = (
        supabase.table("chat_history")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at")
        .execute()
    )

    return result.data


# ==========================
# Memory
# ==========================

def save_memory(user_id, key, value):

    supabase.table("memory").upsert(
        {
            "user_id": user_id,
            "memory_key": key,
            "memory_value": value
        }
    ).execute()


def load_memory(user_id):

    result = (
        supabase.table("memory")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    return result.data
