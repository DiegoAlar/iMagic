/*
This page render dynamic content, It shows the list of classes title
and image, it has commented the code used with Detect Dabels from aws which
was replaced by Custom Labels
*/

const aws = require('aws-sdk');


aws.config.update({
    accessKeyId: process.env.NEXT_PUBLIC_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.NEXT_PUBLIC_AWS_SECRET_ACCESS_KEY,
    region: process.env.NEXT_PUBLIC_AWS_REGION
});


function changeHandler() {
    eraseHandler();
    let prevpic = document.querySelector('#prevPicture');
    let pics = document.querySelector('input[type=file]').files;
    function readAdd(pic) {
        let reader = new FileReader();
        reader.addEventListener("load", function() {
            let image = new Image();
            image.height = 100;
            image.title = pic.name;
            image.src = this.result;
            prevpic.appendChild( image );
        }, false);
        reader.readAsDataURL(pic);
        
        reader.onloadend = () => {
            let rekognition = new aws.Rekognition();
            let params = {
                Image: {
                    Bytes: getBinary(reader.result),
                },
                //MaxLabels: 2,
                MinConfidence: 90.0,
            };
            //rekognition.detectLabels(params, function(err, data) {
            
            // rekognition.detectLabels(params, function(err, data) {
            //     if (err) {
            //         console.log(err, err.stack);
            //     } else {
            //         callLabels(data.Labels);
            //         bringTitles(data.Labels);
            //     }

            // });
            // custom labels **********************************************

            let params2 = {
                Image: { /* required */
                  Bytes: getBinary(reader.result),
                },
                ProjectVersionArn: "arn:aws:rekognition:us-east-2:017784105438:project/manually-labeled-images/version/manually-labeled-images.2020-06-16T13.55.40/1592333741191",
                MaxResults: 10,
                MinConfidence: 50.0,
              };
              rekognition.detectCustomLabels(params2, function(err, data) {
                if (err) {
                    console.log(err, err.stack);
                } else {
                    callLabels(data.CustomLabels);
                    bringTitles(data.CustomLabels);
                }
              });

              // custom labels **************************************************************
        }
        
        
    }

    if (pics) {
        Array.prototype.forEach.call(pics, readAdd);
    }
}

function getBinary(encodedFile) {
    let type_img = encodedFile.split(';')[0]
    let base64Image;
    let type_im;
    if (type_img.includes('jpeg')) {
        base64Image = encodedFile.split("data:image/jpeg;base64,")[1];
        type_im = "image/jpeg"
    } else {
        base64Image = encodedFile.split("data:image/png;base64,")[1];
        type_im = "image/png"
    }
    //let base64Image = encodedFile.split("data:image/png;base64,")[1];
    let binaryImg = atob(base64Image);
    let lenght = binaryImg.length;
    let ab = new ArrayBuffer(lenght);
    let ua = new Uint8Array(ab);
    for (var i = 0; i < lenght; i++) {
        ua[i] = binaryImg.charCodeAt(i);
    }
    let blob = new Blob([ab], {
        type: type_im
    });
    return ab;

}

function callLabels(liLabels) {
    let textLabell = document.createTextNode("Related Labels:");
    let node_la = document.createElement("p")
    node_la.appendChild(textLabell);
    document.getElementById("labelsList").appendChild(node_la);
    liLabels.forEach(ele => {
        let node = document.createElement("span");
        node.className = "badge badge-dark"; 
        let textLabel = document.createTextNode(ele.Name);
        node.appendChild(textLabel);
        document.getElementById("labelsList").appendChild(node);

    });

}

function bringTitles(liLabels){
    let all_courses = []
    let str_url = 'http://127.0.0.1:8000/elastic/'
    let labels_array = []
    liLabels.forEach ((lab) => {
        labels_array.push(lab.Name)
    });
    if (labels_array.length === 0) {
        alert('There are no courses for this picture, try uploading a different one!');
    } else {
        console.log('enterrrrrrrrrrrrrrrrrrrr');

        const url = str_url + labels_array.toString()
        fetch(url)
        .then(response => response.json())
        .then(data => {
            data.forEach((course) => {
                // let course = data[key]
                let divcol = document.createElement("div");
                divcol.className = "column";
                let node_div = document.createElement("div");
                node_div.className = "card";
                node_div.style = "width: 18rem;"
                let node_div1 = document.createElement("div");
                node_div1.className = "card-header";
                node_div.appendChild(node_div1);
                let node_img = document.createElement("img");
                node_img.className = "card-img-top"
                node_img.src = course['class_image']
                node_div.appendChild(node_img);
                let node_div2 = document.createElement("div");
                node_div2.className = "card-body"
                let node_h = document.createElement("h5");
                node_h.className = "card-title"
                let textLabel = document.createTextNode(course['class_title']);
                node_h.appendChild(textLabel);
                node_div2.appendChild(node_h);
                let node_a = document.createElement("a");
                node_a.className = "btn btn-primary"
                node_a.href = course['class_url']
                let textLabela = document.createTextNode("Go to course");
                node_a.appendChild(textLabela);
                node_div2.appendChild(node_a);
                node_div.appendChild(node_div2);
                divcol.appendChild(node_div);
                    //document.getElementById("courseList").appendChild(node_div);
                document.getElementsByClassName("row")[0].appendChild(divcol);
            });
        });        
    }

}

const styling = {
    backgroundImage: "linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url('/static/background4.jpg')",
    justifyContent: 'space-evenly',
    display: 'flex',
    backgroundAttachment: 'fixed',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'cover',
}

function eraseHandler() {
    document.getElementsByClassName("row")[0].innerHTML = "";
    document.getElementById("labelsList").innerHTML = "";
    document.getElementById("prevPicture").innerHTML = "";
    
}
const Titles = () => (
    <div>
        <div className="jumbotron text-left" style={styling}>
            <div>
                <h1>Discover Your Next Creative Breakthrough</h1>
                <h5>With just uploading an image.</h5>

                <label htmlFor="browse" className="file-upload">
                <i className="cloud-upload"></i> Upload...
                </label>
                <input id="browse" type="file" onChange={changeHandler} accept="image/*" multiple />
                <p><small>Accepted formats: <i>jpg or png</i></small></p>
                
            </div>
            <div id="prevPicture"></div>
        </div>
        
        <div id="labelsList">
        </div>
        
        <div className="row">
            
        </div>

        <style global jsx>{`

            input[type="file"] {
                display: none;
            }
            .file-upload {
                border: 1px solid #ccc;
                display: inline-block;
                padding: 6px 12px;
                cursor: pointer;
                background-color: #00ff84;
                border-color: #00ff84;
                width: 200px;
                text-align: center;
                font-weight: bold;
                margin-right:5px;
            }

            
            
            #prevPicture img {
                height: 200px;
                width: 200px;
                object-fit:scale-down;
            }
            
            @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
                // fixes stretched images in cards
                .card-deck .card {
                  display: block;
            }
              
                // fixes stretched images in cards
                .card-group .card {
                  display: block;
                }
            }
            
            .column {
            float: left;
            width: 25%;
            padding: 10px 10px;
            }

            
            .row {
                margin-left: 5%;
                margin-right: 5%;
                height:100%;
                
                
                
                
            }

            
            .row:after {
            content: "";
            display: table;
            clear: both;
            }

            
            @media screen and (max-width: 600px) {
            .column {
                width: 100%;
                display: block;
                margin-bottom: 20px;
                }
            }

            
            .card {
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                padding: 16px;
                text-align: center;
                background-color: #f1f1f1;
            }
            .card-header {
                background: #002333;
                height: 50px;
                background-image: url(../../static/Skillshare-logo1.png);
                background-repeat: no-repeat;
                background-size: 40%;

                           
            }
            .card {
                padding: 0px;
            }
            .btn-primary {
                background-color: #00ff84;
                border-color: #00ff84;
                color: #002333;
                font-weight: bold;

            }

            .btn-primary:hover {
                color: #00ff84;
                background-color: #002333;
                border-color: #002333;
            }
            #labelsList {
                margin-left: 125px;
                width: 200px;
            }

            #labelsList span {
                margin-right: 2px;
            }


        
        `}</style>
        
        
        
    </div>

);

export default Titles;