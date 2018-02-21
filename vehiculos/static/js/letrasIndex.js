setInterval('tipografia()',1000);

var actual = 0;

function tipografia() {
	switch (actual) {
		case 0:
			document.getElementById("tipoLetra").style.color = "green";
			document.getElementById("tipoLetra").style.fontFamily = "Arial";
			actual ++;
			break;
		case 1:
			document.getElementById("tipoLetra").style.color = "red";
			document.getElementById("tipoLetra").style.fontFamily = "Impact";
			actual ++;
			break;
		case 2:
			document.getElementById("tipoLetra").style.color = "brown";
			document.getElementById("tipoLetra").style.fontFamily = "sans-serif";
			actual ++;
			break;
		case 3:
			document.getElementById("tipoLetra").style.color = "yellow";
			document.getElementById("tipoLetra").style.fontFamily = "Roboto";
			actual=0;
			break;
	}

}