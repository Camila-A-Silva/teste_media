def verificador_media(media:int|float) -> str:
    if media >= 7:
        return("Aprovado")
    
    elif media < 5:
        return("Reprovado")
    
    elif media < 7 and media >= 5:
        return("Recuperação")
    
if __name__ == "__main__":
    print(verificador_media(6))
    