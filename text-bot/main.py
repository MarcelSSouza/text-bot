from textblob import TextBlob
# from pattern.en import parse, Sentence, modality


texto0=input("Cole o texto que deseja analisar: ")    
texto = TextBlob(texto0)

# fakeoufato=input("Gostaria de analisar se algo é Fake ou Fato? (Y/n)")
# if(fakeoufato=='Y'):
#     texto_fake_ou_fato = parse(texto0, lemmata=True)
#     texto_fake_ou_fato = Sentence(sent)
#     if(modality(sent)>=0.5):
#         print("Isso é pura verdade.")
#     else:
#         print("Isso é Fake News!")

corrigir=input("Você gostaria de corrigir erros de escrita no texto? (Y/n)")
if(corrigir=="Y"):
    print(texto.correct())
    texto=texto.correct()

traduzir=input("Você gostaria de traduzir o texto? (Y/n)")
if(traduzir=="Y"):
    idioma=input("Digite a sigla do idioma para o qual deseja traduzir o texto (en, es, pt, it, fr): ")
    print(texto.translate(to=idioma))

contar_palavras=input("Você gostaria de saber quantas vezes uma determinada palavra aparece no texto? (Y/n)")
if(contar_palavras=="Y"):
    palavra= input("Contar aparicoes da palavra: ")
    print("A palavra "+palavra+" aparece "+ str(texto.word_counts[palavra])+" vezes no texto.")


sentiment=input("Você gostaria de saber qual, segundo nossos cálculos, é o sentimento desse texto? (Y/n)")
if(sentiment=="Y"):
    print(texto.sentiment)
    if(texto.sentiment.polarity>=0.2):
        print("O seu texto parece ser um texto bem alegre :)")
    if(texto.sentiment.polarity<0.2):
        print("O seu texto parece ser um texto meio pra baixo :(")
    if(texto.sentiment.subjectivity<=0.5):
        print("O seu texto parece ser um texto baseado em fatos concretos :)")
    if(texto.sentiment.subjectivity>0.5):
        print("O seu texto parece ser um texto de opinião :(")
