# Lista Duplamente Encadeada
Lista duplamente encadeada desenvolvida na disciplina Estruturas de Dados

## Autores: Yano e Marina

## Funcionamento

A Lista Duplamente Encadeada foi implementada utilizando duas classe: Element e LinkedList,
a primeira para servir de preenchimento para a lista e a segunda a lista propriamente dita.

Os métodos da lista podem ser divididos em quatro: Métodos de Apoio, Métodos de Adição, Métodos de Deleção e Métodos do Cursor.

Falando primeiramente dos métodos de apoio, o principal deles é o método <em>get_cursor_position()</em>, que serve para conseguir a posição atual do cursor, além da função óbvia que ele executa, este método também é utilizado em casos que é preciso percorrer a lista e recuperar a posição de um determinado elemento, como é o caso de <em>position_of()</em>, ou então, para o cálculo de posição em <em>go_to_position()</em>, <em>forward()</em> e <em>backward()</em>, ambos Métodos de Cursor que iremos tratar mais adiante. Além desse método temos também <em>is_full()</em> e <em>"is_empty()"</em>, que indicam a lotação da lista e permitem o lançamento de exceções conforme o seu retorno.

Nos métodos de adição...