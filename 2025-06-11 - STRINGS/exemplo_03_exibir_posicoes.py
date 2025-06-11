'''
   Programa para detectar as posições de uma palavra (ou letra) dentro de um texto.
'''

strTexto = 'Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, ' \
   'que se destaca por sua sintaxe clara, legibilidade e simplicidade, sendo amplamente utilizada ' \
   'tanto por iniciantes quanto por programadores experientes. Criada por Guido van Rossum e lançada ' \
   'oficialmente em 1991, Python foi desenvolvida com a proposta de ser uma linguagem fácil de aprender ' \
   'e utilizar, sem abrir mão de poder e versatilidade. Seu nome curioso vem do grupo britânico de comédia ' \
   '"Monty Python", e não de uma cobra, como muitos pensam. Desde sua criação, Python vem crescendo em ' \
   'popularidade e se consolidando como uma das linguagens mais importantes da atualidade, especialmente ' \
   'por sua ampla gama de aplicações. Uma das principais características de Python é sua sintaxe simples, ' \
   'que se assemelha à linguagem humana, permitindo que os desenvolvedores escrevam menos linhas de código ' \
   'para realizar tarefas complexas. Essa simplicidade faz com que Python seja frequentemente escolhida como ' \
   'primeira linguagem em cursos de programação e universidades ao redor do mundo. Além disso, Python é uma ' \
   'linguagem de código aberto, o que significa que seu código-fonte é livremente acessível, permitindo que ' \
   'qualquer pessoa possa usá-la, modificá-la e distribuí-la. Isso contribuiu para a criação de uma comunidade ' \
   'ativa e colaborativa que mantém e expande constantemente a linguagem por meio de bibliotecas, frameworks ' \
   'e ferramentas. Outra grande vantagem de Python é sua enorme versatilidade: ela é utilizada em diversas áreas ' \
   'da tecnologia, como desenvolvimento web, análise de dados, inteligência artificial, automação de tarefas, ' \
   'desenvolvimento de jogos, ciência de dados, machine learning, computação científica, entre outras. Frameworks ' \
   'como Django e Flask permitem o desenvolvimento rápido de aplicações web, enquanto bibliotecas como Pandas, ' \
   'NumPy e Matplotlib são amplamente utilizadas para análise e visualização de dados. Já em machine learning e ' \
   'inteligência artificial, bibliotecas como TensorFlow, Keras e Scikit-learn fazem de Python a linguagem dominante ' \
   'nesse campo. A grande adoção de Python por empresas de tecnologia, startups e universidades também contribui para ' \
   'sua popularidade. Empresas como Google, Facebook, Netflix e Spotify utilizam Python em diversos projetos, tanto em ' \
   'desenvolvimento interno quanto em produtos finais. Além disso, sua compatibilidade com outras linguagens e sistemas, ' \
   'junto com a grande quantidade de recursos disponíveis, torna Python uma excelente escolha para integrar tecnologias distintas. ' \
   'Python também é conhecida por sua portabilidade, podendo ser executada em diferentes sistemas operacionais como Windows, Linux ' \
   'e macOS sem necessidade de alterações significativas no código. Com atualizações frequentes e uma filosofia de design baseada ' \
   'na clareza, concisão e legibilidade, Python continua evoluindo, com novas versões que aprimoram o desempenho e expandem suas ' \
   'funcionalidades. Diante de tudo isso, é fácil entender por que Python é considerada uma das linguagens mais influentes e valiosas ' \
   'do mundo da programação, sendo ideal tanto para projetos simples quanto para sistemas de grande escala. Seu crescimento constante ' \
   'e sua capacidade de adaptação a novas demandas tecnológicas garantem que Python continuará sendo uma peça central no futuro da computação.'


strPalavra = input('Digite Palavra: ').lower().strip()

#intTamanho = len(strTexto)
#print(f'O texto possui {intTamanho} caracteres.')

intQtOcorrencias = strTexto.lower().count(strPalavra)
print(f'A palavra {strPalavra} aparece {intQtOcorrencias} vezes no texto.')

intPosicao  = 0
for i in range(intQtOcorrencias):
   intPosicao = strTexto.lower().find(strPalavra, intPosicao)

   print(intPosicao)

   intPosicao += len(strPalavra)

