console.log('Trabalhando com listas');

// const salvador = 'Salvador';
// const saoPaulo = 'São Paulo';
// const rioDeJaneiro = 'Rio de Janeiro';

const listaDeDestinos = new Array(
    'Salvador',
    'São Paulo',
    'Rio de Janeiro'
);

listaDeDestinos.push('Curitiba'); //Adicionando um item na lista


console.log("Destinos possíveis:");
// console.log(salvador, saoPaulo, rioDeJaneiro);
listaDeDestinos.splice(1,1);//Seleciona quantos elementos deletar e depois seleciona sua posição de inicio que ira começar a excluir
console.log(listaDeDestinos);
console.log(listaDeDestinos[1]);
