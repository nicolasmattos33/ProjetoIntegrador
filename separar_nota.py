def salvar_relatorio(conteudo_lista):
    nome_arquivo = "relatorio_final_notas.txt"
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("RESULTADOS DA ANÁLISE ACADÊMICA \n")
            f.write("-" * 40 + "\n")
            for linha in conteudo_lista:
                f.write(linha + "\n")
        print(f"\n[OK] Relatório gerado com sucesso: {nome_arquivo}")
    except Exception as e:
        print(f"\n[ERRO] Falha ao salvar o arquivo: {e}")
def main():
    # simulacao
    dados_alunos = {
        "Nicolas Soares": [9.5, 8.0, 10.0, "texto_errado"],
        "Vitor Domingos": [10.0, 9.5, 9.8],
        "Pedro Ezequiel": [4.0, 5.5, None, 6.0],
        "Vinicius Domingos": [2.0, 3.5]
    }

    print("Iniciando processamento dos alunos...")
    print("-" * 40)

    relatorio_acumulado = []

    for nome, notas_sujas in dados_alunos.items():
        notas_limpas = validar_e_limpar_notas(notas_sujas)
        media = calcular_media_aluno(notas_limpas)
        status = classificar_desempenho(media)
        resultado = f"ALUNO: {nome:<15} | MÉDIA: {media:>5.2f} | STATUS: {status}"
        print(resultado)
        relatorio_acumulado.append(resultado)

    salvar_relatorio(relatorio_acumulado)

if _name_ == "_main_":
    main()