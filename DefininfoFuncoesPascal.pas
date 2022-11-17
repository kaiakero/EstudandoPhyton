program funcoes;
    const TAM =5;
    type vetor = array [1..TAM] of integer;
    var
    v : vetor;
    k,i : integer;
    
    {function soma (a,b : real) : real;
        begin
            soma := a + b;
        end;
    function maior (a,b : real) : real; 
        begin
            if a > b then
                maior = a;
            if b > a then
                maior = b; 
        end;
    procedure linha (x : real, c : char;)}
    procedure troca(var va, vb : integer);
        var aux : integer;
        begin
            aux := vb;
            vb := va;
            va := aux;
        end;    
    
    procedure le_vetor (var v : vetor );
        var i : integer;
        begin 
            writeln('Informe os valores');
            for i := 1 to TAM do
                readln(v[i]);
        end;  
    procedure exibe_vetor (v : vetor);
        var i : integer;
        begin
            writeln('Valores armazenados');
            for i := 1 to TAM do
                writeln('v[',i,']= ',v[i]);
        end;
    procedure classifica (var v : vetor);
        begin
            for k:=1 to tam do
                for i:=1 to TAM-1 do
                    if v[i] > v[i+1] then
                        troca(v[i],v[i+1]);
                        
                    
                
            
        end;
begin
    le_vetor(v);
    classifica(v);
    exibe_vetor(v);
    readln();
  
end.

