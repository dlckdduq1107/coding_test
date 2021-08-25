function solution(new_id) {
    var answer = '';
    let dup = /([a-z0-9-_.]+)/g;
    new_id = new_id.toLowerCase();

    let dupList = new_id.match(dup);
    let id = dupList.join("");
    console.log(dupList);

    let conti = /([.]{2,})/g;

    id = id.replace(conti,".");
    
    
    let dotCheck = /(^[.]+)|([.]+$)/g;
    id = id.replace(dotCheck,"");
    

    if(id === "") id = "a";
    
    if(id.length >= 16){
        id = id.slice(0,15);
        id = id.replace(dotCheck,"");
    }

    if(id.length<=2){
        let temp = id[id.length-1];
        while(id.length !== 3){
            id+= temp;
        }
    }
    console.log(id);
    return answer;
}

solution("z-+.^.")
