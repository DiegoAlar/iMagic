/*
This page render dynamic content, It shows projects by a given project id
or all projects
*/
function showLabels() {
    let url;
    let search_value = document.getElementById("myInput").value;
    if (search_value === "all") {
        url = 'http://127.0.0.1:8000/projects/elastic/'
    } else {
        url = 'http://127.0.0.1:8000/projects/elastic/' + search_value;
    }
    let node_div = document.getElementById("projectList");
    while (node_div.hasChildNodes()) {
        node_div.removeChild(node_div.lastChild);
    }
    fetch(url)
        .then(response => response.json())
        .then(data => {
            data.forEach((image_value) => {
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
                node_img.src = image_value['image_url'];
                node_div.appendChild(node_img);
                let node_div2 = document.createElement("div");
                node_div2.className = "card-body"
                let node_h = document.createElement("h5");
                node_h.className = "card-title"
                let textLabel = document.createTextNode(image_value['project_title']);
                node_h.appendChild(textLabel);
                node_div2.appendChild(node_h);
                let node_p = document.createElement("p");
                node_p.className = "card-text";
                let textLabelp = document.createTextNode(image_value['class_title']);
                node_p.appendChild(textLabelp);
                node_div2.appendChild(node_p);
                let div_container = document.createElement("div");
                div_container.className = "boxNew"
                
                Object.keys(image_value['image_labels']).forEach((label) => {
                    let node = document.createElement("span");
                    node.className = "badge badge-dark";
                    //let label_list = Object.values(label);
                    let labelName = label + ': ' + Number((image_value['image_labels'][label]).toFixed(1)) // Number((6.688689).toFixed(1));
                    let textLabel = document.createTextNode(labelName);
                    node.appendChild(textLabel);
                    div_container.appendChild(node);
                
                document.getElementsByClassName("row")[0].appendChild(divcol);
                });
                node_div2.appendChild(div_container);
                let nodeDivSmall = document.createElement("div");
                let nodeSmall = document.createElement("small");
                let textLabelSmall = document.createTextNode("* Label: Confidence");
                nodeSmall.appendChild(textLabelSmall);
                nodeDivSmall.appendChild(nodeSmall);
                node_div2.appendChild(nodeDivSmall);
                let node_a = document.createElement("a");
                node_a.className = "btn btn-primary"
                node_a.href = image_value['project_url'];
                let textLabela = document.createTextNode("Go to project");
                node_a.appendChild(textLabela);
                node_div2.appendChild(node_a);
                node_div.appendChild(node_div2);
                divcol.appendChild(node_div);
            });
        });
}     

const Projects = () => (
    <div>
        <input type="text" placeholder="Type project id or all to show all projects..." id="myInput" />
        <button type="button" className="btn-primary" onClick={showLabels}>Search</button>
        <div id="projectList" className="row"></div>

        <style global jsx>{`
            #myInput {
                margin-top: 10%;
                margin-left: 37%;
                width: 310px;
            }
            .card-img-top {
                float: left;
                margin-left: 15%;
                margin-top: 15%;
                width:  200px;
                object-fit: cover;
            }
            pre {
                text-align: left;
                
            }
            span {
                margin-right: 2px;
            }

            input[type="file"] {
                display: none;
            }

            #projectList {
                margin-top: 30px;
            }
            .file-upload {
                border: 1px solid #ccc;
                display: inline-block;
                padding: 6px 12px;
                cursor: pointer;
            }
            .boxNew {
                width: 100%;
                height: auto;
                // overflow: scroll;
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
                width: 32%;
                padding: 10px 10px;
            }

            
            .row {
                margin-left: 15%;
                margin-right: 10%;
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
                margin-top: 10px;
            }

            .btn-primary:hover {
                color: #00ff84;
                background-color: #002333;
                border-color: #002333;
        `}</style>
    </div>
);

export default Projects;
