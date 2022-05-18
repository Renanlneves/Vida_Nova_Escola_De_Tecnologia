programa
{
	
	funcao inicio()
	{
		
		inteiro idade, jovem_m_id, jov_cont = 0, adu_m = 0, id_adu_m = 0, med_adu_id_m = 0
		inteiro id_jv = 0, jv_cont = 0, alt_adu_m = 0, med_adu_alt_m = 0, med_ex_id_m = 0
		inteiro id_jv_f = 0, id_jv_m = 0, ex_f = 0, id_ex_f = 0, id_ex_m = 0
		real md_id_jv = 0.0, md_id_jv_f = 0.0, pes_adu_f = 0.0, pes_adu_m = 0.0, med_adu_pes_m = 0.0, med_ex_pes_m = 0.0
		inteiro jov_f = 0, jov_m = 0, med_ex_id_f = 0, ex_m = 0, alt_ex_m = 0
		inteiro altura = 0, alt_adu_f = 0, med_adu_alt_f = 0
		inteiro alt_jov_f = 0, med_alt_jov_f = 0, alt_jov_m = 0, med_alt_jov_m = 0, med_ex_alt_m = 0
		inteiro adu_f = 0, id_adu_f = 0, med_adu_id_f = 0, alt_ex_f = 0, med_ex_alt_f = 0
		real med_jov_f = 0.0, med_jov_m = 0.0, peso=0.0, pes_jov_f = 0.0, med_pes_jov_f = 0.0, pes_ex_m = 0.0
		real pes_jov_m = 0.0, med_pes_jov_m = 0.0, med_adu_pes_f = 0.0, pes_ex_f = 0.0,  med_ex_pes_f = 0.0, imc = 0.0
		inteiro a = 0, b = 0, c = 0, d = 0, f = 0, g = 0, h = 0, i = 0, j = 0
		caracter refazer, sexo
		logico fem_jov = falso, mas_jov = falso, fem_adu = falso, mas_adu = falso
		logico fem_ex = falso, mas_ex = falso



		//inicio do laço de repetição 
		faca{
		
		//coletando dados do usuario		
		escreva("idade?\n")
		leia (idade)
		limpa()

			//perguntando o genero
		escreva ("Qual o seu genero? \"m\" ou \"f\"\n")
		leia (sexo)
		limpa()

		escreva ("Qual é seu peso\n")
		leia (peso)
		limpa()

		escreva("Qual sua altura (em cemtimetros)?\n")
		leia (altura)
		limpa()
		
		//separando em grupos
		//se idade maior que 18 anos será jovem.
		se (idade >= 18 e idade < 32 ){
			
			id_jv = id_jv + idade
			
			jv_cont = jv_cont + 1 

			se (sexo == 'f'){
				jov_f = jov_f + 1
				id_jv_f = id_jv_f + idade
				pes_jov_f = pes_jov_f + peso
				alt_jov_f = alt_jov_f + altura
				}
			senao {
				jov_m = jov_m + 1
				id_jv_m = id_jv_m + idade
				pes_jov_m = pes_jov_m + peso
				alt_jov_m = alt_jov_m + altura
				}
			
			}
			
		//se idade maior que 32 e menor que 61 anos será adulto 
		senao se (idade >= 32 e idade < 61){

			se (sexo == 'f'){
				adu_f = adu_f ++
				id_adu_f = id_adu_f + idade
				pes_adu_f = pes_adu_f + peso
				alt_adu_f = alt_adu_f + altura
				}

			senao {
				adu_m = adu_m ++
				id_adu_m = id_adu_m + idade
				pes_adu_m = pes_adu_m + peso
				alt_adu_m = alt_adu_m + altura
				
				}
			
			
			}
		//se a idade não se encaixa em nenhum anterior, ela deve ser maior que 61
		senao {
				se (sexo == 'f'){
				ex_f = ex_f ++
				id_ex_f = id_ex_f + idade
				pes_ex_f = pes_ex_f + peso
				alt_ex_f = alt_ex_f + altura
				}

				senao {
				ex_m = ex_m ++
				id_ex_m = id_ex_m + idade
				pes_ex_m = pes_ex_m + peso
				alt_ex_m = alt_ex_m + altura
				}
			}
	
			

		
		


			//calculando as medias por grupo.
			//jovem
			se (idade > 18 e idade < 32){
			md_id_jv = (id_jv / jv_cont)}
			
			//media de mulheres jovens
			se ((idade > 18 e idade < 32) e sexo == 'f'){ 
			fem_jov = verdadeiro
			med_jov_f = (id_jv_f / jov_f)
			med_pes_jov_f = (pes_jov_f / jov_f)
			med_alt_jov_f = (alt_jov_f / jov_f)
			}
			
			//media de homens jovens
			se ((idade > 18 e idade < 32) e sexo == 'm'){
			mas_jov = verdadeiro 
			med_jov_m = (id_jv_m / jov_m)
			med_pes_jov_m = (pes_jov_m / jov_m)
			med_alt_jov_m = (alt_jov_m / jov_m)
			}

			//media de mulheres adultas
			se ((idade > 32 e idade < 61) e sexo == 'f'){
				fem_adu = verdadeiro
				med_adu_id_f = (id_adu_f / adu_f)
				med_adu_pes_f = (pes_adu_f / adu_f)
				med_adu_alt_f = (alt_adu_f / adu_f)
				}

			se ((idade > 32 e idade < 61) e sexo == 'm'){
				mas_adu = verdadeiro
				med_adu_id_m = (id_adu_m / adu_m)
				med_adu_pes_m = (pes_adu_m / adu_m)
				med_adu_alt_m = (alt_adu_m / adu_m)
				}

			se (idade >= 62 e sexo == 'f'){
				fem_ex = verdadeiro
				med_ex_id_f = (id_ex_f / ex_f)
				med_ex_pes_f = (pes_ex_f / ex_f)
				med_ex_alt_f = (alt_ex_f / ex_f)
				}

			se (idade >= 62 e sexo == 'm'){
				mas_ex = verdadeiro
				med_ex_id_m = (id_ex_m / ex_m)
				med_ex_pes_m = (pes_ex_m / ex_m)
				med_ex_alt_m = (alt_ex_m / ex_m)
				}

			imc = (peso / (altura * altura) * 10000 )
			escreva ("\tSeu imc é de ",imc)
			
			se (imc > 18.5 e imc < 24.9){
				escreva ("\n\tSeu peso está ok!!")
				} 
			senao se(imc < 18.4){
				escreva ("\n\tVocê está abaixo do peso!")
				}

			senao se(imc > 24.9){
				escreva ("\n\tVocê está com Sobrepeso!")
			}
			senao{}
			




			
			
		//frase perguntando se o usuario quer refazer a pesquisa
		escreva ("\n\nGostaria de fazer uma nova pesquisa? (\"s\" para sim ou \"n\" para não)\n")
		leia (refazer)
		limpa()
		
		
		//fim do laço. Abaixo deve vir a condição "faca enquanto"
		} 
		//enquanto o usuario não responder "n" na pergunta anterior, o programa recomeça
		enquanto (refazer != 'n')
		limpa()





		escreva("\n\n")
		
		// XXXXX TABELA XXXXXX

			
		enquanto (a <= 31){
			
		escreva("__")
		a = a++
		}
		

		escreva ("\n|\t\t\tMedias por Grupo\t\t\t|\n")

		enquanto (b <= 31){
			
		escreva("__")
		b = b++
		}

		escreva("\n│     GRUPO\t")
		escreva("│     IDADE  \t")
		escreva("│     PESO   \t")
		escreva("│     ALTURA\t│\n")

		enquanto (c <= 31){
			
		escreva("__")
		c = c++}
		
			se (fem_jov == verdadeiro){
			escreva("\n│  Joven Mulher ")
			escreva("│      ",med_jov_f,"     ")
			escreva("│      ",med_pes_jov_f,"     ")
			escreva("│      ",med_alt_jov_f,"      │\n")}

				senao{
					escreva("\n│  Joven Mulher ")
					escreva("│       00      ")
					escreva("│       00      ")
					escreva("│      000      │\n")
					}

		enquanto (d <= 31){
			
		escreva("__")
		d = d++}

			se (mas_jov == verdadeiro){
			escreva("\n│  Joven Homem  ")
			escreva("│      ",med_jov_m,"     ")
			escreva("│      ",med_pes_jov_m,"     ")
			escreva("│      ",med_alt_jov_m,"      │\n")}

			senao{
					escreva("\n│  Joven Homem  ")
					escreva("│       00      ")
					escreva("│       00      ")
					escreva("│      000      │\n")
					}

			enquanto (f <= 31){
			
		escreva("__")
		f = f++}
			se (fem_adu == verdadeiro){
			escreva("\n│ Adulto Mulher ")
			escreva("│       ",med_adu_id_f,"      ")
			escreva("│      ",med_adu_pes_f,"     ")
			escreva("│      ",med_adu_alt_f,"      │\n")
			}
				senao{
					escreva("\n│ Adulto Mulher ")
					escreva("│       00      ")
					escreva("│       00      ")
					escreva("│      000      │\n")
					}
		enquanto (g <= 31){
			
		escreva("__")
		g = g++}
			se (mas_adu == verdadeiro){
			escreva("\n│ Adulto Homem  ")
			escreva("│       ",med_adu_id_m,"      ")
			escreva("│      ",med_adu_pes_m,"     ")
			escreva("│      ",med_adu_alt_m,"      │\n")}

				senao{
					escreva("\n│ Adulto Homem  ")
					escreva("│       00      ")
					escreva("│       00      ")
					escreva("│      000      │\n")}
			

		enquanto (h <= 31){
			
		escreva("__")
		h = h++}


			se (fem_ex == verdadeiro){
			escreva("\n│ Expert Mulher ")
			escreva("│       ",med_ex_id_f,"      ")
			escreva("│      ",med_ex_pes_f,"     ")
			escreva("│      ",med_ex_alt_f,"      │\n")}

			senao{
					escreva("\n│ Expert Mulher ")
					escreva("│       00      ")
					escreva("│       00      ")
					escreva("│      000      │\n")}

		
		enquanto (i <= 31){
			
		escreva("__")
		i = i++}

			se (mas_ex == verdadeiro){
			escreva("\n│ Expert Homem  ")
			escreva("│       ",med_ex_id_m,"      ")
			escreva("│      ",med_ex_pes_m,"     ")
			escreva("│      ",med_ex_alt_m,"      │\n")}

			senao{
				escreva("\n│ Expert Homem  ")
					escreva("│       00      ")
					escreva("│       00      ")
					escreva("│      000      │\n")
				}

			
		enquanto (j <= 31){
			
		escreva("__")
		j = j++}

		escreva("\n\n\n")


		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 4402; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */