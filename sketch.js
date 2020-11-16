let mutationRate = 0.01;
let totalPopulation = 380; 

let population = [];
let matingPool = []; 

let input, button; 

let generation = 0; 

function setup() {
  createCanvas(400, 400);
  
  for(let i = 0; i < totalPopulation; i++){
    population.push( new DNA()); 
  }
}

function draw() {
  background('#FC8826');
  text('Genetic algorithm',50,100)
  text('in solving magic squares',50,130)
  translate(150,120); 
  GA();
  text(`total generations: ${generation}`, -40,180)
  text(`total individuals: ${generation * totalPopulation}`, -40,210)

  generation++;
  if(generation > 50){
    noLoop(); 
  }
}


function drawTable(gene){
  stroke('white');  
  fill('#EB394C')

  textSize(20)
  strokeWeight(3)
  for(let i= 0; i < 9; i++){
    x  = i * 30; 
    if(x < 90){
    rect(x,30,30)
    text(gene[i], x + 10 , 50)
    }
    if(x  >=  90 && x < 180 ){
    rect(x - 90,60,30)
    text(gene[i], x - 90 + 10 , 80)

    }
    if(x >= 180 && x < 270){
    rect(x - 180, 90, 30)
    text(gene[i], x - 180 + 10 , 110)

    }
  }
  /*
  textSize(10); 
    ellipse(115,45,20)
    ellipse(115,105,20)
    ellipse(115,75,20)
    ellipse(10,155,20)
    ellipse(40,155,20)
    ellipse(70,155,20)
  fill('#EB394C')
  noStroke()
  text(gene[0] + gene[1] + gene[2], 110, 50)
  text(gene[3] + gene[4] + gene[5], 110, 80)
  text(gene[6] + gene[7] + gene[8], 110, 110)
  text(gene[0] + gene[3] + gene[6],  5, 160)
  text(gene[1] + gene[4] + gene[7], 35, 160)
  text(gene[2] + gene[5] + gene[8], 65,160)
  fill('white')
  */

}


function GA(){
  for (let i = 0; i < population.length; i++) {
    population[i].fit();
  }
  let matingPool = []; 
  
  for (let i = 0; i < population.length; i++) {
    let n = int(population[i].fitness * 150);
  for (let j = 0; j < n; j++) {
      matingPool.push(population[i]);
    }
  }
  
  for (let i = 0; i < population.length; i++) {
    let a = int(random(matingPool.length));
    let b = int(random(matingPool.length));
    let partnerA = matingPool[a];
    let partnerB = matingPool[b];
    let child = partnerA.crossover(partnerB.gene,partnerA.gene);
    child.mutate(mutationRate);
    population[i] = child;
    drawTable(child.gene);
  }
 
  
}