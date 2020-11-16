class DNA {

 constructor(){
  this.gene  = this.randomicArray(); 
  this.fitness = 0;  
 }

 fit(){
   
  if((this.gene[0] + this.gene [1] +this.gene[2]) == 15){
    this.fitness ++
  }
  if(this.gene[3] + this.gene [4]+this.gene[5] == 15){
    this.fitness ++
  }
  if(this.gene[6] + this.gene [7]+this.gene[8] == 15){
    this.fitness ++
  }
  if(this.gene[0] + this.gene [4]+ this.gene[8] == 15){
    this.fitness ++
  }if(this.gene[2] + this.gene [4]+this.gene[6] == 15){
    this.fitness ++
  }
  if(this.gene[1] + this.gene [4]+this.gene[7] == 15){
    this.fitness ++
  }
  if(this.gene[0] + this.gene [3]+this.gene[6] == 15){
    this.fitness ++
  }
  if(this.gene[2] + this.gene [5]+this.gene[8] == 15){
    this.fitness ++
  }
  if(this.gene[4] == 5){
    this.fitness ++
  } 
 } 
  
  
 mutate (mutationRate){
    for(let i = 0; i < 9; i++){
      if(random(1) < mutationRate){
        let a = this.gene[int(random(9))];
        let b = this.gene[int(random(9))];

        let rand = this.gene[a]; 
        this.gene[a] = this.gene[b];
        this.gene[b] = rand; 
      }
    }
  }
  
      
  
  
 randomicArray(){
    let res = [];

    while(res.length <= 8){
        let rand = Math.floor(Math.random() * 9) + 1; 
        if(res.indexOf(rand) == -1){
        res.push(rand)}
    } 
    return res
  }
  
  
/**
 * retorna metade os genes de um individuo
 */

fatherGens(res, individual){
    let child  = [];

    for(let i = 0; i < 9; i++){
        if( res.indexOf(i) > -1 ){
            child.push(individual[i])
        }else{
            child.push(NaN)
        }
    }
  
    return child
}

/**
 * Retorna a localização dos genes do pai na cadeia de dna da mae
 */

motherGens(father, mother){
    
    let result = []
    mother.forEach((e,i,a) => {
        if(father.indexOf(father[i]) > -1){
            result.push(i)
        }
    });
    
    return result
}

/**
 * Geração de novo individuo
 */

makeChild(rand, father, mother){

    let aux = [];

    mother.forEach((e,i,a)=>{
        if(father.indexOf(e) > -1 ){
        aux.push(NaN)
        }else{
        aux.push(e)
        }
    });

    let res = []

    for( let i = 0; i <= 9; i++){
        if(!isNaN(father[i])){
            res.push(father[i])
        }
        if(!isNaN(aux[i])){
           res.push(aux[i])
        }
    }

    return {
        m: aux,
        ind: res
    }

 }

selectRandom(n){
    let res = [];

    while(res.length < n ){
        let rand = Math.floor(Math.random() * 9 )
        if(res.indexOf(rand) == -1){
        res.push(rand)}
    }
    return res

}
  crossover(father, mother){
    
   let child  = new DNA(); 
    
   let rand  =  this.selectRandom(4)
   father = this.fatherGens(rand, father)
   mother = this.makeChild(rand,father,mother).m
   let result = this.makeChild(rand,father,mother).ind
   child.gene = result; 
   return child;  
 }
}