# AStar Algorithm Visualization
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![MIT License][license-shield]](https://opensource.org/licenses/MIT)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/wai-han-692305174/)


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
  A* (pronounced "A-star") is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases.
  
  #### Equation
  ```f(n) = g(n) + h(n) ``` where
  > n = the next node on the path
  
  > g(n) = the cost from the start node to the node `n`
  
  > h(n) = heuristic function that estimates the cost of cheapest path from n to   goal


### Built With

* [Python](https://www.python.org)
* [Pygame](https://www.pygame.org)

<!-- GETTING STARTED -->
## Getting Started

This is how you may set up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
```pip install pygame```

```pip install numpy```

```pip install python-tk```

<!-- USAGE EXAMPLES -->

## Usage

As the current source code mainly focuses on visualization, it is a great idea for people who are learning path finding algorithm, such as [A*](https://en.wikipedia.org/wiki/A*_search_algorithm), [Dijkstra's](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) etc... **Visualizing** is one of the great techniques for learning. You can play around with the code and understand the core idea of what a *path finding algorithm* is.

Unfortunately as of right now, the only possible method is A* algortihm.



<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Note
*If you consider contributing to the project, I'd like to request you to implement the Dijkstra's algorithm firstly.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Email -> wh.kankan13@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Tech with Time](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Choose an Open Source License](https://choosealicense.com)
* [README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
* [Astar Algortithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
* [Dijkstra's Algortihm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
