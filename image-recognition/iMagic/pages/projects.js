//Projects page
import Head from 'next/head';
import Projects from '../components/Projects';

const styling = {
    backgroundImage: "linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url('/static/background4.jpg')",
    justifyContent: 'space-evenly',
    display: 'flex',
    backgroundAttachment: 'fixed',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'cover',
}

const Project = () => (
    <div>
        <Head>
            <meta charset="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
            <title>Skillshare</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/css/bootstrap.min.css"></link>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css"></link>
            
        </Head>
    
        <body>
            <nav className="navbar navbar-light navbar-expand-md">
                <div className="container-fluid">
                    <img src={'/static/Skillshare-logo1.png'} width="15%" height="50%" />
                    <button data-toggle="collapse" className="navbar-toggler" data-target="#navcol-1">
                        <span className="sr-only">Toggle navigation</span><span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navcol-1">
                        <ul className="nav navbar-nav">
                            <li className="nav-item" role="presentation"><a className="nav-link active text-white" href="/">Classes</a></li>
                            <li className="nav-item" role="presentation"><a className="nav-link text-white" href="/projects">Projects</a></li>
                            <li className="nav-item" role="presentation"></li>
                        </ul>
                    </div>
                </div>
                
            </nav>
            
            <Projects/>
            <div className="footer-dark">
                <footer>
                    <div className="container">
                        <div className="row">
                            <div className="col item social"><a href="https://www.linkedin.com/in/diego-andr%C3%A9s-alarcon-valencia-748442168/"><i className="icon ion-social-linkedin"></i></a><a href="https://www.linkedin.com/in/marylgomez/"><i className="icon ion-social-linkedin"></i></a></div>
                        </div>
                        <p className="copyright">Skillshare-Rocket team 2020</p>
                    </div>
                </footer>
            </div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/js/bootstrap.bundle.min.js"></script>
        </body>
        <style jsx>{`
            .social {
                margin-left: -8%;
            }
            .copyright {
                margin-left: -6%;
            }
            .footer-basic {
                padding: 40px 0;
                background-color: #ffffff;
                color: #4b4c4d;
            }
            
            .footer-basic ul {
                padding: 0;
                list-style: none;
                text-align: center;
                font-size: 18px;
                line-height: 1.6;
                margin-bottom: 0;
            }
            
            .footer-basic li {
                padding: 0 10px;
            }
            
            .footer-basic ul a {
                color: inherit;
                text-decoration: none;
                opacity: 0.8;
            }
            
            .footer-basic ul a:hover {
                opacity: 1;
            }
            
            .footer-basic .social {
                text-align: center;
                padding-bottom: 25px;
            }
            
            .footer-basic .social > a {
                font-size: 24px;
                width: 40px;
                height: 40px;
                line-height: 40px;
                display: inline-block;
                text-align: center;
                border-radius: 50%;
                border: 1px solid #ccc;
                margin: 0 8px;
                color: inherit;
                opacity: 0.75;
            }
            
            .footer-basic .social > a:hover {
                opacity: 0.9;
            }
            
            .footer-basic .copyright {
                margin-top: 15px;
                text-align: center;
                font-size: 13px;
                color: #aaa;
                margin-bottom: 0;
            }

            .footer-clean {
                padding: 50px 0;
                background-color: #fff;
                color: #4b4c4d;
            }
            
            .footer-clean h3 {
                margin-top: 0;
                margin-bottom: 12px;
                font-weight: bold;
                font-size: 16px;
            }
            
            .footer-clean ul {
                padding: 0;
                list-style: none;
                line-height: 1.6;
                font-size: 14px;
                margin-bottom: 0;
            }
            
            .footer-clean ul a {
                color: inherit;
                text-decoration: none;
                opacity: 0.8;
            }
            
            .footer-clean ul a:hover {
                opacity: 1;
            }
            
            .footer-clean .item.social {
                text-align: right;
            }
            
            @media (max-width:767px) {
                .footer-clean .item {
                text-align: center;
                padding-bottom: 20px;
                }
            }
            
            @media (max-width: 768px) {
                .footer-clean .item.social {
                text-align: center;
                }
            }
            
            .footer-clean .item.social > a {
                font-size: 24px;
                width: 40px;
                height: 40px;
                line-height: 40px;
                display: inline-block;
                text-align: center;
                border-radius: 50%;
                border: 1px solid #ccc;
                margin-left: 10px;
                margin-top: 22px;
                color: inherit;
                opacity: 0.75;
            }
            
            .footer-clean .item.social > a:hover {
                opacity: 0.9;
            }
            
            @media (max-width:991px) {
                .footer-clean .item.social > a {
                margin-top: 40px;
                }
            }
            
            @media (max-width:767px) {
                .footer-clean .item.social > a {
                margin-top: 10px;
                }
            }
            
            .footer-clean .copyright {
                margin-top: 14px;
                margin-bottom: 0;
                font-size: 13px;
                opacity: 0.6;
            }

            .footer-dark {
                height: 20%;
                padding: 50px 0;
                color: #f0f9ff;
                background-color: #002333;
                position: fixed;
                bottom: 0%;
                width: 100%;
            }
            
            .footer-dark h3 {
                margin-top: 0;
                margin-bottom: 12px;
                font-weight: bold;
                font-size: 16px;
            }
            
            .footer-dark ul {
                padding: 0;
                list-style: none;
                line-height: 1.6;
                font-size: 14px;
                margin-bottom: 0;
            }
            
            .footer-dark ul a {
                color: inherit;
                text-decoration: none;
                opacity: 0.6;
            }
            
            .footer-dark ul a:hover {
                opacity: 0.8;
            }
            
            @media (max-width:767px) {
                .footer-dark .item:not(.social) {
                text-align: center;
                padding-bottom: 20px;
                }
            }
            
            .footer-dark .item.text {
                margin-bottom: 36px;
            }
            
            @media (max-width:767px) {
                .footer-dark .item.text {
                margin-bottom: 0;
                }
            }
            
            .footer-dark .item.text p {
                opacity: 0.6;
                margin-bottom: 0;
            }
            
            .footer-dark .item.social {
                text-align: center;
            }
            
            @media (max-width:991px) {
                .footer-dark .item.social {
                text-align: center;
                margin-top: 20px;
                }
            }
            
            .footer-dark .item.social > a {
                font-size: 20px;
                width: 36px;
                height: 36px;
                line-height: 36px;
                display: inline-block;
                text-align: center;
                border-radius: 50%;
                box-shadow: 0 0 0 1px rgba(255,255,255,0.4);
                margin: 0 8px;
                color: #fff;
                opacity: 0.75;
            }
            
            .footer-dark .item.social > a:hover {
                opacity: 0.9;
            }
            
            .footer-dark .copyright {
                text-align: center;
                padding-top: 24px;
                opacity: 0.3;
                font-size: 13px;
                margin-bottom: 0;
            }

            .navbar.navbar-light.navbar-expand-md {
            }
            
            .navbar.navbar-light.navbar-expand-md {
            background-color: #002333;
            }
            
            .navbar-light .navbar-brand {
            background-image: url(../../static/logoSkill.png);
            }
            
            img {
            }
            
            img {
            widht: 10px;
            }
            
            img {
            padding: 0px;
            margin-left: -50px;
            }
            
            .navbar-light .navbar-nav .active > .nav-link, .navbar-light .navbar-nav .nav-link.active, .navbar-light .navbar-nav .nav-link.show, .navbar-light .navbar-nav .show > .nav-link {
            }
            
            .navbar-light .navbar-nav .active > .nav-link, .navbar-light .navbar-nav .nav-link.active, .navbar-light .navbar-nav .nav-link.show, .navbar-light .navbar-nav .show > .nav-link {
            }
            
            .navbar-light .navbar-nav .active > .nav-link, .navbar-light .navbar-nav .nav-link.active, .navbar-light .navbar-nav .nav-link.show, .navbar-light .navbar-nav .show > .nav-link {
            /*font-style: campton bold;*/
            }
            
            .jumbotron.text-left {
            /*margin-left: 20px;*/
            }
            
            .h1, h1 {
            margin-left: 50px;
            }
            
            p {
            text-align: center;
            margin-left: 50px;
            }
            
            .btn:not(:disabled):not(.disabled) {
            margin-left: 50px;
            }
            
            .jumbotron.text-left {
            height: 300px;
            }
            
            .btn:not(:disabled):not(.disabled) {
            }
            
            .btn:not(:disabled):not(.disabled) {
            background-color: #00ff84;
            border-color: #00ff84;
            width: 400px;
            }
            
            img {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .jumbotron.text-left {
            }
            
            .btn:not(:disabled):not(.disabled) {
            font-size: x-large;
            }
            .jumbotron text-left {
                backgroundImage: linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url('/static/background4.jpg');
                justify-content: space-evenly;
                display: flex;
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }

            body {
                margin-bottom: 20%;
            }

            
          
        `}</style>
    </div>
)
export default Project;