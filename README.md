# Lista Duplamente Encadeada
Lista duplamente encadeada desenvolvida na disciplina Estruturas de Dados

## Autores: Yano e Marina

## Funcionamento

A Lista Duplamente Encadeada foi implementada utilizando duas classe: Element e LinkedList,
a primeira para servir de preenchimento para a lista e a segunda a lista propriamente dita.

Os métodos da lista podem ser divididos em quatro: Métodos de Apoio, Métodos de Adição, Métodos de Deleção e Métodos do Cursor.

Falando primeiramente dos métodos de apoio, o principal deles é o método <em>get_cursor_position()</em>, que serve para conseguir a posição atual do cursor, além da função óbvia que ele executa, este método também é utilizado em casos que é preciso percorrer a lista e recuperar a posição de um determinado elemento, como é o caso de <em>position_of()</em>, ou então, para o cálculo de posição em <em>go_to_position()</em>, <em>forward()</em> e <em>backward()</em>, ambos Métodos de Cursor que iremos tratar mais adiante. Além desse método temos também <em>is_full()</em> e <em>is_empty()</em>, que indicam a lotação da lista e permitem o lançamento de exceções conforme o seu retorno.

Os <strong>Métodos de Adição</strong>. Todos possuem uma verificação para ver se a lista já está cheia utilizando o método de apoio <em>is_full()</em>, caso a resposta seja verdadeira uma exceção é levantada, além disso, todos adicionam uma unidade ao atributo "counter". Tanto <em>set_last()</em> quanto em <em>set_first()</em> o cursor não é movimentada quando os métodos são chamadas, apenas caso o elemento seja o primeiro adicionado na lista. Em <em>add_next()</em> o cursor se move para o elemento adicionado, a adição funciona apenas apontando o atributo "next" do elemento adicionado para o "next" do cursor, o "next" do cursor para o elemento e o "previous" do elemento para o cursor e logo em seguida, adicionando o elemento como cursor da Lista. A mesma lógica é utilizada por <em>add_in_position()</em>, que utiliza <em>add_next()</em> como base, apenas com o adicional de ir para a posição anterior a que o usuário deseja adicionar o elemento, utilizando o método <em>go_to_position()</em>, um método de cursor.

Os <strong>Métodos de Deleção</strong>. O primeiro método de deleção é o <em>delete_current()</em> que apenas pega o "next" e o "previous" do cursor, e muda seus atributos, respectivamente, para o "previous" e o "next" do cursor. Os métodos <em>delete_first()</em> e <em>delete_last()</em> funcionam da mesma forma que seus equivalentes na adição. O mesmo vale para <em>delete_in_position()</em> que também utiliza <em>go_to_position()</em> como base. Já no caso de <em>delete_by_value()</em> duas funções são utilizadas de apoio, a primeira <em>position_of()</em> que retorna a posição de um elemento pelo seu valor e passando essa posição como parâmetro de <em>delete_in_position()</em>, conseguimos executar o propósito da nossa função.

Os <strong>Métodos de Cursor</strong>. Todas as funções de cursor, com exceção de <em>go_to_first()</em> e <em>go_to_last()</em>, utilizam a função <em>get_cursor_position()</em> para executar cálculos de posição em relação ao cursor, em <em>go_to_position()</em> o valor do sinal determina se a função irá utilizar <em>forward()</em> e <em>backward()</em> para o deslocamento.