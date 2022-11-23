<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com"> 
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
    <link href="https://fonts.googleapis.com/css2?family=Cabin:wght@400;700&display=swap" rel="stylesheet">
    <title>Skylanders Cards</title>
</head>
<style>
    body{
        font-family: 'Cabin', serif;
    }
    p {
        font-size: 22px;
    }
    .cards{
        display: flex;
        gap:15px;
        flex-wrap: wrap;
    }
    .card{
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        height:8.56cm;
        width: 5.39cm;
        background: rgb(4,0,59);
        background: linear-gradient(180deg, rgba(4,0,59,1) 17%, rgba(200,85,250,1) 100%);
        border-radius: 5px;
    }
    .skylanderImgContainer{
        /* background-color: green; */
        /* opacity: .5; */
        height: 8.56cm;
        width: 5.39cm;
        margin-top: 40px;
        text-align: center;
    }

    img{
        max-width: 178px;
        max-height: 175px
    }
    
    .skylanderNameContainer{
        position: relative;
        border-radius: 0px 0px 5px 5px;
        text-align: center;
        background-color:rgba(228, 162, 250, 0.85);
        width: 5.39cm;
        padding: 5px 0px;
    }   
</style>
<body>
    <div class="cards">
    <?php
    
        $s1Aantal = 37;
        $s2Aantal = 62;
        $s3Aantal = 75;
        $s4Aantal = 80;
        $s5Aantal = 70;
        $s6Aantal = 41;
        for( $i = 0; $i < $s6Aantal; $i++){
            echo '<div class="card">
                        <div class="skylanderImgContainer">
                            <img src="" alt="" class="skylanderImg">
                        </div>
                        <div class="skylanderNameContainer">
                            <p class="skylanderName"></p>
                        </div>
                    </div>';
        }
    ?>
    </div>
    <script>
        function readTextFile(file, callback) {
            var rawFile = new XMLHttpRequest();
            rawFile.overrideMimeType("application/json");
            rawFile.open("GET", file, true);
            rawFile.onreadystatechange = function() {
                if (rawFile.readyState === 4 && rawFile.status == "200") {
                    callback(rawFile.responseText);
                }
            }
            rawFile.send(null);
        }

        readTextFile("skylanderSerie/json/s6.json", function(text){
            let SKYLANDERID = 0
            var theImg = document.getElementsByClassName('skylanderImg');
            var data = JSON.parse(text);
            let nameHtml = document.getElementsByClassName("skylanderName")
            let imgHtml = document.getElementsByClassName("skylanderImg")
            for(i= 0; i < Object.keys(data).length; i++){
                console.log(data);
                nameHtml[i].innerHTML = data[SKYLANDERID+i].name;
                imgHtml[i].src = data[SKYLANDERID+i].img
            }
        });
        


    </script>
</body>
</html>