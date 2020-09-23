function mtrxConstructor (n){
  do{
    var M = new Array(n);
    for(var i=0; i<n;i++){
      M[i] = new Array(n);
      for (var j=0; j<n; j++){
        M[i][j]=0
        
      }
    }
  }while(n % 2 == 0); 

  return M
}
function printMtrx (M,n){
  for(var i=0;i<n;i++){
    document.write('<br>')
    for (var j=0; j<n ; j++){
      if (M[i][j]<10){
       document.write('0'+M[i][j]+' ')
      }else {
         document.write(M[i][j]+' ')
      }
     
    }
 }
}
//printMtrx (mtrxConstructor (7),7);
function dataInsert (M,n){
  var a = 1 ,y = 0,x = 0;
  var lim = n-1;
    do{
      if( a==1 ){ 
      	y = 0; 
        x = parseInt(n/2);
        //document.write('b'); 
      }else if( y == 0 ){
        if ( x == lim ){
          y++;
          //document.write('1');
        }else { 
          y = lim;
          x++;
          //document.write('2');
        }
      }else if ( x == lim ){
        x = 0;
        y--;
        //document.write('3');
      }else {
      	if ( M[y][x]!=0 ){
        	x++;
        	y--;
          //document.write('4');
          if ( M[y][x]!= 0 ){
            y=y+2;
            //document.write('4');
            x--;
          }
        }
      }
      M[y][x] = a++;
      //printMtrx (M,n);
      //document.write('<br>')
    }while ( a<=n*n );
  
}
M = mtrxConstructor (5);
dataInsert ( M,5 );
printMtrx ( M,5 )
