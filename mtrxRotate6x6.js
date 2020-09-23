var n=6;var a=1;
function mtrxConstructor (n){
  do{
    var M = new Array(n);
    for(var i=0; i<n;i++){
      M[i] = new Array(n);
      for (var j=0; j<n; j++){
        M[i][j]=a++
      }
    }
  }while(n % 2 != 0); 
  return M
}
function MTRXprint (M,n){
  for(var i=0;i<n;i++){
      document.write('<br>');
      for (var j=0; j<n ; j++){
        if (M[i][j]<10){
         document.write('0'+M[i][j]+' ')
        }else {
         document.write(M[i][j]+' ')
        }
      }
   }
}
Mat = mtrxConstructor (6);
M = mtrxConstructor (6);
MTRXprint (Mat,6);
document.write('<br>');
function dataInsert (M,n){
  var y=0, x=0, aux, aux2, t, a=n*n, b=0,c=0 , mid=n/2, jump=mid*2;
    for (var i=0;i<mid*2;i++){
  	while ( b<mid ){
      //segundo-cuarto
      aux=M[y][x];
      if (c<mid){
      aux2=M[y+3][x+3]
      }else{ aux2=M[y-3][x+3] }
      t=aux2;
      aux2=aux;
      t2=aux;
      aux=t;
      M[y][x]=t;
      if (c<mid){
      M[y+3][x+3]=t2
      }else { M[y-3][x+3]=t2 }
      x++;
      b++
      //MTRXprint (M,6);
      //document.write('<br>');
    }
    y++;
    b=0;
    x=0;
    c++
  }
}
dataInsert (Mat,6);
MTRXprint (Mat,6);
