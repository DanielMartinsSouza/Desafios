console.log('Trabalhando com listas');

const listaDeDestinos = new Array(
    'Salvador',
    'São Paulo',
    'Rio de Janeiro'
);

const idadeComprador = 15;
const estaAcompanhada = true;
const temPassagemComprada = true;

console.log("Destinos possíveis:");
console.log(listaDeDestinos);

// if (idadeComprador >= 18) {
//     console.log("Comprador maior de idade");
//     listaDeDestinos.splice(1, 1); //Seleciona quantos elementos deletar e depois seleciona sua posição de inicio que ira começar a excluir

// } else if (estaAcompanhada) {
//     console.log("Comprador está acompanhado");
//     listaDeDestinos.splice(1, 1); //Seleciona quantos elementos deletar e depois seleciona sua posição de inicio que ira começar a excluir
// } else {
//     console.log("Não é maior de idade, então não posso vender!!")
// }


if (idadeComprador >= 18 || estaAcompanhada) {
    console.log("Boa viagem!!");
    listaDeDestinos.splice(2, 1); //Seleciona quantos elementos deletar e depois seleciona sua posição de inicio que ira começar a excluir

} else {
    console.log("Não é maior de idade, então não posso vender!!");
}
console.log(listaDeDestinos);

console.log("Embarque: \n\n");

if(idadeComprador >= 18 && temPassagemComprada){
    console.log("Boa viagem!!");
} else{
    console.log("Você não pode embarcar");
}

