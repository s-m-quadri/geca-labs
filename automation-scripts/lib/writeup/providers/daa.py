"""DAA (Design and Analysis of Algorithms) writeup question banks."""

from __future__ import annotations

import os
import random
from typing import List, Tuple

from lib.lab_course import LabCourse
from lib.writeup.context import WriteupContext
from lib.writeup.source import sanitize_code_for_latex
from lib.writeup.util import format_matrix_rows, make_int_array


class DaaWriteupProvider:
    listings_style = "py"
    source_kind_label = "Python"
    source_subsection_title = "Source code"
    digest_instruction = "Hand-run or compute using the lab's source code behavior."

    def subjective_questions(self, lab_num: int, title: str, rng: random.Random | None = None) -> List[str]:
        common = {
            0: [
                "What are lists and tuples in Python?",
                "What are functions and how do you define one in Python?",
                "Explain the difference between mutable and immutable types in Python.",
                "What is a lambda function in Python?",
                "What is list comprehension in Python? Give a brief example.",
            ],
            1: [
                "Define recursion and iteration.",
                "State the base case and inductive step for factorial(n).",
                "Explain stack overflow risk in recursive calls.",
                "What makes iteration safer than recursion in Python?",
            ],
            2: [
                "Define Divide-and-Conquer. Where does merge sort use it?",
                "State merge sort's time and space complexity.",
                "When does the iterative (bottom-up) variant help?",
            ],
            3: [
                "Define binary search and its precondition (sorted?).",
                "State best/avg/worst-case time in Big-O (one line).",
                "How do bounds change when key < arr[mid]?",
            ],
            4: [
                "Define fractional knapsack and density (value/weight).",
                "Why sorting by ratio is optimal.",
                "State when item is taken partially.",
            ],
            5: [
                "Define MST and Prim's choice rule.",
                "Why MST called 'spanning' and 'tree'?",
                "What's difference between Graph and Tree? Are all trees graphs? Are the terms fuzzy?",
                "What is a key[] array used for in Prim's?",
                "How many edges are in an MST of V vertices?",
            ],
            6: [
                "Define union-find with path compression.",
                "What does union by rank prevent?",
                "Kruskal's sorting criterion for edges.",
            ],
            7: [
                "Define multistage graph and stages concept.",
                "Why is backward DP used here?",
                "What value is set at the sink initially and why?",
            ],
            8: [
                "Contrast 1-indexed vs 0-indexed DP tables.",
                "What is recorded in the path[] array?",
                "When is an edge considered absent in cost matrix?",
            ],
            9: [
                "Define prefix-free code.",
                "Why does Huffman pick two least-frequent nodes?",
                "What determines a symbol's code length?",
            ],
            10: [
                "State the N-Queens constraint succinctly.",
                "What does is_safe check (3 checks, one phrase)?",
                "How many solutions exist for N=8?",
            ],
        }
        items = list(common.get(lab_num, [f"Briefly state two key concepts of: {title}."]))
        if rng is not None and items:
            if len(items) >= 4:
                items = rng.sample(items, 3)
            else:
                rng.shuffle(items)
        return items

    def objective_questions(self, lab_num: int, rng: random.Random) -> List[str]:
        Q: List[str] = []
        if lab_num == 1:
            n = rng.randint(4, 10)
            Q += [
                f"For factorial({n}), how many multiplications are performed?",
                f"In recursion, how many stack frames exist at peak for n={n}?",
            ]
        elif lab_num == 2:
            n = rng.randrange(8, 33, 2)
            Q += [
                f"For merge sort on n={n}, how many levels of splitting occur?",
                f"At the last merge level, how many subarrays are merged?",
            ]
        elif lab_num == 3:
            n = rng.choice([11, 15, 17, 31])
            idx = rng.randint(0, n - 1)
            Q += [
                f"Sorted array size n={n}. If key is at index {idx}, what is the maximum mid checks in iterative binary search?",
                f"If key absent, what is the worst-case number of mid checks for n={n}?",
            ]
        elif lab_num == 4:
            W = rng.randint(20, 60)
            items = rng.randint(3, 6)
            Q += [
                f"With capacity W={W} and {items} items, which greedy sorting key is used?",
                "When do we take a fractional part of an item (state the condition)?",
            ]
        elif lab_num == 5:
            V = rng.randint(4, 7)
            Q += [
                f"In Prim's on a connected graph with V={V}, how many edges in MST?",
                "What criterion picks the next vertex (state in <=1 line)?",
            ]
        elif lab_num == 6:
            e = rng.randint(5, 10)
            Q += [
                f"Kruskal sorts how many edges if E={e}?",
                "Write the stopping condition for Kruskal in terms of edges/vertices.",
            ]
        elif lab_num == 7:
            nodes = rng.randint(6, 10)
            Q += [
                f"In backward DP on a multistage graph with {nodes} nodes, which node's dist is set to 0 initially?",
                "What is stored in next_node[i] (<=1 line)?",
            ]
        elif lab_num == 8:
            N = rng.randint(6, 10)
            Q += [
                f"For 1->N shortest path with N={N}, what is cost[N] initialized to?",
                "What does path[i] represent (<=1 line)?",
            ]
        elif lab_num == 9:
            unique = rng.randint(3, 6)
            Q += [
                f"For a string with {unique} distinct symbols, what is the range of possible code lengths in Huffman?",
                "Is Huffman code unique for a given frequency table? (Yes/No + 1 line)",
            ]
        elif lab_num == 10:
            N = rng.choice([4, 5, 6, 8])
            Q += [
                f"For N={N}, how many queens are placed per valid solution?",
                "Name the three conflict directions checked before placing a queen (<=1 line).",
            ]
        else:
            Q += ["State any two key learnings from this lab."]
        return Q

    def code_digest_questions(self, lab_num: int, rng: random.Random) -> List[str]:
        Q: List[str] = []
        if lab_num == 0:
            a = make_int_array(rng, 5, 1, 9)
            Q += [
                f"Hand-run a Python function sum(arr) on arr={a}. Show running total after each addition.",
                "Write 2 lines of pseudocode to reverse a list in-place.",
            ]
        elif lab_num == 1:
            n = rng.randint(4, 8)
            Q += [
                f"Trace factorial_recursive({n}) showing the call stack (one line per call).",
                f"Compute factorial_iterative({n}) and list intermediate result after each multiplication.",
            ]
        elif lab_num == 2:
            arr = make_int_array(rng, rng.choice([6, 8, 10]), 1, 50)
            Q += [
                f"Run one full merge_sort_recursive on arr={arr}. Write the sequence of merged subarrays.",
                "State the final sorted array.",
            ]
        elif lab_num == 3:
            n = rng.choice([9, 11, 15])
            arr = sorted(make_int_array(rng, n, 1, 60, distinct=True))
            key = rng.choice(arr)
            miss = rng.randint(61, 90)
            Q += [
                f"On arr={arr}, trace binary_search_iterative for key={key}: write low, high, mid at each step.",
                f"Repeat for an absent key={miss} and show termination condition.",
            ]
        elif lab_num == 4:
            items = [(rng.randint(10, 120), rng.randint(5, 30)) for _ in range(rng.randint(3, 5))]
            W = rng.randint(20, 60)
            Q += [
                f"Given items (value,weight)={items} and capacity W={W}, order items by ratio and compute total value taken.",
                "Specify which item (if any) is taken fractionally and by what fraction.",
            ]
        elif lab_num == 5:
            V = rng.randint(4, 6)
            graph = [[0] * V for _ in range(V)]
            for i in range(V):
                for j in range(i + 1, V):
                    w = rng.randint(1, 9) if rng.random() < 0.7 else 0
                    if w == 0:
                        if i == j - 1:
                            w = rng.randint(1, 9)
                    graph[i][j] = graph[j][i] = w
            mat_rows = [
                [graph[i][j] if graph[i][j] != 0 else "INF" if i != j else 0 for j in range(V)]
                for i in range(V)
            ]
            mat_latex = format_matrix_rows(mat_rows)
            Q += [
                "Run Prim's algorithm starting at vertex 0 on the following adjacency matrix (use 0 on diagonal, \\infty for no edge):",
                mat_latex,
                "List the edges picked in order with weights and state the final MST total weight.",
            ]
        elif lab_num == 6:
            V = rng.randint(4, 6)
            E = rng.randint(V, V * (V - 1) // 2)
            edges: List[Tuple[int, int, int]] = []
            used = set()
            while len(edges) < E:
                u, v = rng.sample(range(V), 2)
                if u > v:
                    u, v = v, u
                if (u, v) in used:
                    continue
                used.add((u, v))
                w = rng.randint(1, 15)
                edges.append((w, u, v))
            Q += [
                f"Apply Kruskal's to edges (w,u,v)={edges}. Show the sorted order and union steps. Write the resulting MST.",
                "Give the total weight of the MST.",
            ]
        elif lab_num == 7:
            n = rng.randint(6, 8)
            INF = 10**9
            cost = [[INF] * n for _ in range(n)]
            for i in range(n - 1):
                edges_out = rng.randint(1, min(3, n - i - 1))
                targets = rng.sample(range(i + 1, n), edges_out)
                for j in targets:
                    cost[i][j] = rng.randint(1, 12)
            cost[n - 1][n - 1] = 0
            mat_rows = [
                [(0 if (i == j == n - 1) else (cost[i][j] if cost[i][j] != INF else "INF")) for j in range(n)]
                for i in range(n)
            ]
            mat_latex = format_matrix_rows(mat_rows)
            Q += [
                "Using backward DP on the following cost matrix (\\infty = no edge), compute dist[0] and the path from 0->(sink).",
                mat_latex,
                "If no feasible path exists due to missing edges, explicitly state it and explain why (in 1-2 lines).",
                "List dist[i] for all i (or mark unreachable with infty).",
            ]
        elif lab_num == 8:
            N = rng.randint(6, 9)
            edges_l: List[Tuple[int, int, int]] = []
            for i in range(1, N):
                out_deg = rng.randint(1, min(3, N - i))
                targets = rng.sample(range(i + 1, N + 1), out_deg)
                for j in targets:
                    edges_l.append((i, j, rng.randint(1, 9)))
            matrix = [[0] * (N + 1) for _ in range(N + 1)]
            for u, v, w in edges_l:
                matrix[u][v] = w
            mat_rows = [row[1:] for row in matrix[1:]]
            mat_latex = format_matrix_rows([[c if c != 0 else "INF" for c in row] for row in mat_rows])
            Q += [
                f"For N={N} with the following 1-indexed cost matrix (\\infty = no edge), compute cost[1] and the 1->N path as in the lab code:",
                mat_latex,
                "If no feasible path exists, state so and justify briefly.",
                "Write cost[i] for i=1..N.",
            ]
        elif lab_num == 9:
            alphabet = rng.sample(
                list("abcdefghijklmnopqrstuvwxyz"),
                rng.randint(4, 7),
            )
            text = "".join(rng.choices(alphabet, k=rng.randint(12, 20)))
            Q += [
                f"Build the Huffman tree for text=\"{text}\". Write the code for each character and the encoded length.",
                "Is this encoding optimal given these frequencies? (justify in 1 line)",
            ]
        elif lab_num == 10:
            N = rng.choice([4, 5, 6])
            Q += [
                f"Run the backtracking solver for N={N}. Show one valid board configuration as a 0/1 matrix.",
                "Briefly list the (row,col) placements in order.",
            ]
        else:
            Q += ["Hand-run the core algorithm on a small example of your choice."]
        return Q

    def lab_source_tuple(self, lab_num: int, ctx: WriteupContext) -> Tuple[str, str] | None:
        mapping = {
            1: "1.recursion.py",
            2: "2.merge_sort.py",
            3: "3.binary_search.py",
            4: "4.fractional_knapsack.py",
            5: "5.prims.py",
            6: "6.kruskal.py",
            7: "7.multistage_graph.py",
            8: "8.multistage_graph.py",
            9: "9.huffman.py",
            10: "10.eight_queens.py",
        }
        fname = mapping.get(lab_num)
        if not fname:
            return None
        path = os.path.join(ctx.scripts_root, "labs", fname)
        if not os.path.exists(path):
            return None
        try:
            with open(path, encoding="utf-8") as f:
                code = sanitize_code_for_latex(f.read())
            return fname, code
        except OSError:
            return None


def create_provider(course: LabCourse) -> DaaWriteupProvider:
    _ = course
    return DaaWriteupProvider()
