<script>
    // @ts-nocheck

    import { onMount } from "svelte";
    import Chart from "chart.js/auto";
    import { data } from "../data/data.js";

    let canvas;
    let ctx;
    let chart;

    let innerWidth;

    onMount(() => {
        ctx = canvas.getContext("2d");

        chart = new Chart(ctx, {
            type: "radar",
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false,

                elements: {
                    line: {
                        borderWidth: 3,
                        tension: 0.4,
                    },
                },
                scales: {
                    r: {
                        beginAtZero: true,
                        ticks: {
                            count: 4,
                        },
                    },
                },
                plugins: {
                    legend: {
                        display: true,
                        position: innerWidth > 1024 ? "right" : "bottom",
                    },
                },
            },
        });
    });

    let current = 'All';
    function changeChart(toShow) {
        if (chart) {
            let startShow, endShow;
            if (toShow == "A") {
                current = "A";
                startShow = 0;
                endShow = 2;
            } else if (toShow == "B") {
                current = "B";
                startShow = 3;
                endShow = 6;
            } else if (toShow == "C") {
                current = "C";
                startShow = 7;
                endShow = 11;
            } else if (toShow == "D") {
                current = "D";
                startShow = 12;
                endShow = 20;
            } else if (toShow == "E") {
                current = "E";
                startShow = 21;
                endShow = 29;
            } else if (toShow == "F") {
                current = "F";
                startShow = 30;
                endShow = 41;
            } else if (toShow == "G") {
                current = "G";
                startShow = 42;
                endShow = 48;
            } else {
                // All
                current = "All";
                startShow = 0;
                endShow = 48;
            }

            for (let i = 0; i <= 48; i++) {
                if (startShow <= i && i <= endShow) {
                    chart.setDatasetVisibility(i, true);
                } else {
                    chart.setDatasetVisibility(i, false);
                }
            }
            chart.update();
        }
    }

    $: if (innerWidth) {
        if (chart) {
            if (window.innerWidth < 1024) {
                chart.options.plugins.legend.position = "bottom";
            } else {
                chart.options.plugins.legend.position = "right";
            }
        }
    }
</script>

<svelte:window bind:innerWidth />

<div class="header section">
    <h1>
        Beyond the Gamer Stereotype: A Typology of Live Streamers and Their
        Entrepreneurial Pathways
    </h1>
    <h3>By Claudia Chin</h3>
    <p>
        Part of a dissertation submitted to the Singapore University of Technology and Design (SUTD) in fulfilment of the requirement for the degree of Master of Science in Technology Entrepreneurship 2019.
    </p>
</div>

<div class="section">
    <p>
        The radar chart below displays the factors of comparison that each live streamer was evaluated based on. The buttons below show how the streamers were eventually grouped together.
    </p>
    <div class="buttons">
        <button class="{current === 'All' ? 'selected' : ''}" on:click={() => changeChart("All")}>All</button>
        <button class="{current === 'A' ? 'selected' : ''}" on:click={() => changeChart("A")}>Group A</button>
        <button class="{current === 'B' ? 'selected' : ''}" on:click={() => changeChart("B")}>Group B</button>
        <button class="{current === 'C' ? 'selected' : ''}" on:click={() => changeChart("C")}>Group C</button>
        <button class="{current === 'D' ? 'selected' : ''}" on:click={() => changeChart("D")}>Group D</button>
        <button class="{current === 'E' ? 'selected' : ''}" on:click={() => changeChart("E")}>Group E</button>
        <button class="{current === 'F' ? 'selected' : ''}" on:click={() => changeChart("F")}>Group F</button>
        <button class="{current === 'G' ? 'selected' : ''}" on:click={() => changeChart("G")}>Group G</button>
    </div>
</div>

<div class="chart section">
    <canvas bind:this={canvas} />
</div>

<div class="footer section">
    <p>Copyright 2023. Claudia Chin.</p>
</div>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Akshar:wght@300;700&display=swap");

    h1,
    h3,
    p {
        font-family: "Akshar", sans-serif;
        text-align: start;
        margin: 0;
        color: #121212;
    }

    h1 {
        font-size: 32px;
        font-weight: bold;
        font-style: normal;
    }

    h3 {
        font-size: 24px;
        font-weight: bold;
        font-style: normal;
    }

    p {
        font-size: 16px;
        font-weight: normal;
        font-style: normal;
        margin: 4px 0;
        white-space: pre-line;
    }

    .section {
        padding: 32px;
    }

    .buttons button {
        font-family: "Akshar", sans-serif;
        font-size: 16px;
        border: none;
        padding: 8px 16px;
        border-radius: 8px;
    }

    .buttons button.selected {
        border: solid 2px #121212;
    }

    .buttons button:nth-child(2) {
        color: white;
        background: rgb(197, 30, 58);
    }
    .buttons button:nth-child(3) {
        color: white;
        background: rgb(255, 79, 0);
    }
    .buttons button:nth-child(4) {
        background: rgb(255, 191, 0);
    }
    .buttons button:nth-child(5) {
        color: white;
        background: rgb(86, 130, 3);
    }
    .buttons button:nth-child(6) {
        color: white;
        background: rgb(49, 140, 231);
    }
    .buttons button:nth-child(7) {
        color: white;
        background: rgb(138, 43, 226);
    }
    .buttons button:nth-child(8) {
        background: rgb(255, 145, 175);
    }

    .chart {
        position: relative;
        margin: auto;
        height: 80vh;
    }
</style>
