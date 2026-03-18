
 Levantamento de Requisitos
Requisitos Funcionais (RF)

RF01 -Notas: O sistema deve ser capaz de receber e percorrer listas de notas de diferentes tamanhos por aluno.

RF02 - Calcular Média: O sistema deve calcular a média das notas fornecidas para cada aluno.

RF03 - Identificar: O sistema deve classificar automaticamente se o aluno está em "Aprovação", "Recuperação" ou "Destaque".

RF04 - Validar Dados: O sistema deve identificar e tratar dados incompletos, vazios ou corrompidos antes do processamento.

RF05 - Gerar Relatório: O sistema deve exportar um arquivo .txt formatado contendo os resultados consolidados da análise acadêmica.

Requisitos Não-Funcionais (RNF)

RNF01 - Modularização: O código deve ser estruturado em módulos independentes, separando a lógica de processamento da execução principal (main).

RNF02 - Tratamento de Erros: O sistema deve ser resiliente a falhas de entrada, garantindo que o programa não interrompa a execução ao encontrar um dado inválido.

RNF03 - Organização e Legibilidade: O código deve seguir boas práticas de escrita para facilitar a manutenção futura.

RNF04 - Confiabilidade: Os cálculos e a classificação de status devem ser precisos para apoiar as decisões da coordenação.

Regras de Negócio (RN)

RN01 - Variabilidade de Atividades: O sistema deve aceitar quantidades variáveis de notas, pois cada aluno pode ter um histórico de atividades diferente.

RN02 - Alerta de Atenção: Alunos em recuperação devem ser destacados com prioridade no processamento para intervenção pedagógica.

RN03 - Reconhecimento de Desempenho: Alunos com as melhores médias devem ser identificados de forma automática para ações de reconhecimento.

RN04 - Persistência de Dados: Toda análise concluída deve obrigatoriamente ser salva no relatório externo para fins de arquivamento e consulta posterior.