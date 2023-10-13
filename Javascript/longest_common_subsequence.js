function lcs(x, y) {
    var s1 = x.length;
    var s2 = y.length;
    var a = new Array(s1+1);
    for(var i=0; i<=s1; i++) {
        a[i] = new Array(s2+1);
        for(var j=0; j<=s2; j++) {
        a[i][j] = 0;
        }
    }
    for(var i=1; i<=s1; i++) {
        for(var j=1; j<=s2; j++) {
        if(x[i-1] == y[j-1]) {
            a[i][j] = a[i-1][j-1] + 1;
        } else {
            a[i][j] = Math.max(a[i-1][j], a[i][j-1]);
        }
        }
    }
    return a[s1][s2];
    }

    var x = "AGGTAB";

    var y = "GXTXAYB";

    console.log(lcs(x, y));
