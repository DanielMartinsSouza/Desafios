console.log('\nTrabalhando com listas');

const listaDeDestinos = new Array(
    'Salvador',
    'São Paulo',
    'Rio de Janeiro'
);

const idadeComprador = 15;
const estaAcompanhada = true;
let temPassagemComprada = false;
const destino = "Salvador";

console.log("\nDestinos possíveis:");
console.log(listaDeDestinos);

const podeComprar = idadeComprador >= 18 || estaAcompanhada == true;

let contador = 0;
let destinoExiste = false;
while(contador < 3){    
    if(listaDeDestinos[contador] == destino){
        console.log("Destino existente!!");
        destinoExiste = true;
        break;
    } else{
        destinoExiste = false;
    }

    contador += 1;
}

console.log("Destino existe: ",destinoExiste);

if(podeComprar && destinoExiste){
    console.log("Boa Viagem!!");
} else{
    console.log("Tivemos um erro!!")
}

for(let i = 0; i < 3; i++){    
    if(listaDeDestinos[i] == destino){
        console.log("Destino existente!!");
        destinoExiste = true;
        break;
    } else{
        destinoExiste = false;
    }

    contador += 1;
}