<!DOCTYPE HTML>
<!--
	Helios by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>ICEBOX - Let's get cookin'</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="ie8.css" /><![endif]-->
	</head>
	<body class="homepage">
		<div id="page-wrapper">

			<!-- Header -->
				<div id="header">

					<!-- Inner -->
						<div class="inner">
							<header>
								<h1><a href="#" id="header_logo">Icebox</a></h1>

								<p>Let's get cookin'</p>
							</header>
							<footer>
								<a href="#banner" id = "gotoingredients" class="button circled scrolly"></a>
								<a href="#recipelist" id = "gotorecipelist" class="button circled scrolly"></a>
								<a href="#" id = "gotoreceipt" class="button circled scrolly"></a>
							</footer>
						</div>

					<!-- Nav 
						<nav id="nav">
							<ul>
								<li><a href="index.html">Home</a></li>
								<li>
									<a href="#">Dropdown</a>
									<ul>
										<li><a href="#">Lorem ipsum dolor</a></li>
										<li><a href="#">Magna phasellus</a></li>
										<li><a href="#">Etiam dolore nisl</a></li>
										<li>
											<a href="#">And a submenu &hellip;</a>
											<ul>
												<li><a href="#">Lorem ipsum dolor</a></li>
												<li><a href="#">Phasellus consequat</a></li>
												<li><a href="#">Magna phasellus</a></li>
												<li><a href="#">Etiam dolore nisl</a></li>
											</ul>
										</li>
										<li><a href="#">Veroeros feugiat</a></li>
									</ul>
								</li>
								<li><a href="left-sidebar.html">Left Sidebar</a></li>
								<li><a href="right-sidebar.html">Right Sidebar</a></li>
								<li><a href="no-sidebar.html">No Sidebar</a></li>
							</ul>
						</nav>
					-->
				</div>

			<!-- Banner -->
			<!-- Display list of ingredients, textbox to add ingredient, a button to delete ingredient -->
				<section id="banner">
					<header>
						<h2>Hi. You're looking at your Icebox.</h2>
						<p>
							Add or remove food items from your fridge.
						</p>
					</header>
						<ul>
							<!--Using HTML list to list ingredients in alphabetical order-->
							<body>
							<div class = "addAndRemove">
								<form action = "/" method="post">
								<label id= "addLabel"><strong>Add ingredients:</strong></label>
								<input id = "addTextBox" type="text" name="ingredients"><br>
								<input type="hidden" value="add" name = "modification">
								<input id = "addButton" type = "submit" value = "Add">
								</form>
								<hr>
								<label id="removeLabel"><strong>Remove ingredients:</strong></label>
							<div class = "containIntAndCheckbox">

							<form action = "/" method="post">
							% for ingredient in ingredients:
							<input class = "checkbox" type="checkbox" value={{ingredient}} name="ingredients">
							<li class = "item">{{ ingredient }}</li><br>
							% end
							</div>
							<input type="hidden" value="remove" name="modification">
							<input id = "removeButton" type="submit" value="Remove">
							</form>
							
							
							</div>
						</ul>
					
					
					<a href="#recipelist" id="gotorecipelist" class="button circled scrolly"></a>
				</body>
				</section>

			<!-- Carousel, where you display all the suitable recipes -->
				<section id = "recipelist" class="carousel">
					<div class="reel">

						% for recipe in recipes: 
						<article>
							<a href="#" class="image featured"><img src="pic01.jpg" alt="" /></a>
							<header>
								<h3><a href="#main">{{ recipe.name }}</a></h3>
							</header>
							<p>{{ ', '.join(recipe.ingredients) }}</p>
						</article>
						% end
					</div>
				</section>

			<!-- Main -->
				<div class="wrapper style2">

					<article id="main" class="container special">
						<a href="#" class="image featured"><img src="pic06.jpg" alt="" /></a>
						<header>
							
							<h2><a href="#"></a>Recipes:</h2>
							% for recipe in recipes:
								</br>
									<h2>{{ recipe.name.title() }}</h2>
									Ingredients:
									<ul style="list-style:circle;">
									% for ingredient in recipe.ingredients:
										<li> {{ ingredient }} </li>
									% end
									</ul>
									</p>
									% if recipe.instructions is not None:
										<p> {{ recipe.instructions }} </p>
									% end
							% end
						</header>
						
					</article>

				</div>

			
			<!-- Footer -->
				<div id="footer">
					<div class="container">
						<div class="row">


						</div>

						<header id="footer_logo">
							<p>Icebox</p>
							<p id="ournames">CJ Moynihan</p>
							<p id="ournames">Daniel Chen</p>
							<p id="ournames">Naeema Ahmed</p>
							<p id="ournames">Ellen Lo</p>

						</header>
						<hr />
						<div class="row">
							<div class="12u">


								

								<!-- Copyright -->
									<div class="copyright">
										<ul class="menu">
											<li>&copy; Untitled. All rights reserved.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
										</ul>
									</div>

							</div>

						</div>

					</div>
				</div>

		</div>

		<!-- Scripts -->
			<script src="jquery.min.js"></script>
			<script src="jquery.dropotron.min.js"></script>
			<script src="jquery.scrolly.min.js"></script>
			<script src="jquery.onvisible.min.js"></script>
			<script src="skel.min.js"></script>
			<script src="util.js"></script>
			<!--[if lte IE 8]><script src="ie/respond.min.js"></script><![endif]-->
			<script src="main.js"></script>

	</body>
</html>
