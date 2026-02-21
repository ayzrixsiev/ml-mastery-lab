from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def generate_female_names(anime_type: str) -> str:
    llm = ChatOllama(
        model="llama3.1:8b", temperature=0.7, base_url="http://127.0.0.1:11434"
    )

    prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a female name expert. Suggest cute Japanese style female names based on their anime personality",
            ),
            ("human", "Give me 5 names for a {anime_type} character."),
        ]
    )

    chain = prompt_template | llm

    response = chain.invoke({"anime_type": anime_type})

    return response.content.strip()


if __name__ == "__main__":
    names = generate_female_names(anime_type="Tsundere")
    print(names)
