#!/usr/bin/env python3
"""Generate publication detail pages and a minimalist index list."""
import os
import html

OUT_DIR = "/Users/lijingjing/personal-website/pub"
os.makedirs(OUT_DIR, exist_ok=True)

# ======================== DATA ========================
# Each pub: id, slug, category, title, authors_html, venue_html, abstract_html, cta_label, cta_url, image
PUBS = [
    # ----- JOURNALS -----
    dict(id="J01", cat="Journal Article", title="Metamaterial robotics",
         slug="metamaterial-robotics", img="metamaterial-robotics.jpg",
         authors="Xiaoyang Zheng, Yuhao Jiang, Mustafa Mete, <strong>Jingjing Li</strong>, et al.",
         venue="<em>Science Robotics</em>, 10(108), 2025",
         abstract="Mechanical metamaterials featuring customized microstructures are increasingly shaping robotic design and functionality, enabling the integration of sensing, actuation, control, and computation within the robot body. This Review outlines how metamaterial design principles — mechanics-inspired architectures, shape-reconfigurable structures, and material-driven functionality — enhance adaptability and distributed intelligence in robotics. The authors discuss how artificial intelligence supports metamaterial robotics design and modeling, advancing systems with complex sensory feedback, learning capability, and adaptive physical interactions. The Review aims to inspire the community to explore the transformative potential of metamaterial robotics, fostering innovations that bridge the gap between materials engineering and intelligent robotics.",
         cta_label="View on Science Robotics", cta_url="https://doi.org/10.1126/scirobotics.adx1519"),

    dict(id="J02", cat="Journal Article", title='Discipline Together with the Self in Kendo: Exploring "Qi" through Mixed Reality and Autoethnography',
         slug="kendo-mr", img="kendo-mr.jpg",
         authors="Karen Furuta, <strong>Jingjing Li</strong>, Tatsuki Fushimi, Yoichi Ochiai",
         venue="<em>Proceedings of the ACM on Computer Graphics and Interactive Techniques</em>, 8(3), 2025 (SIGGRAPH 2025)",
         abstract='In an era where swords are no longer wielded to kill but to enhance human lives, swordfights are not about confronting the opponent in front of you but facing yourself. At the core of modern-day combat lies the cultivation of virtues such as etiquette, patience, and mental unity — principles similarly embraced in kendo. Resonating with these principles of kendo, the authors embarked on an exploration of "self," "sword," and "qi" in mixed reality. The author served as a model for this digital human practice of kendo alone in mixed reality using the developed application. This experience of engaging with oneself, sword, and qi has been shared through autoethnography. The researchers hope this documentation contributes to personal growth and enrichment of the spiritual culture in society.',
         cta_label="View on ACM", cta_url="https://doi.org/10.1145/3736776"),

    dict(id="J03", cat="Journal Article", title="Mapping the educational metaverse: a bibliometric analysis of trends, influences and future directions",
         slug="educational-metaverse", img="educational-metaverse.jpg",
         authors="Clarice Wider, Walton Wider, Yoon Fah Lay, Leilei Jiang, <strong>Jingjing Li</strong>, et al.",
         venue="<em>Kybernetes</em>, 2025",
         abstract="<strong>Purpose.</strong> This study investigates the evolving role of metaverse technologies in education through bibliometric analysis. It aimed to identify trends, influential studies and emerging areas within the application of the metaverse in educational contexts.\n\n<strong>Design / methodology.</strong> A systematic bibliometric analysis was conducted using the Web of Science (WoS) database. Citation, co-citation and co-word analyses were applied to identify key authors, institutions and thematic clusters in the literature on metaverse technologies in education.\n\n<strong>Findings.</strong> The results indicate a significant increase in research interest from 2020 to 2023, with China, the US and South Korea leading in output. Three main clusters emerged from the co-citation analysis: technological development, educational integration and the adoption of metaverse technologies. Co-word analysis revealed five thematic areas: immersive learning environments and advanced educational technologies.\n\n<strong>Originality.</strong> This study offers a systematic identification of current trends, research gaps and future directions for metaverse educational applications. It provides a valuable resource for educators, policymakers and researchers, emphasizing the need for further exploration of the long-term impact and ethical considerations of using immersive technologies in learning environments.",
         cta_label="View on Emerald", cta_url="https://doi.org/10.1108/K-11-2024-2965"),

    dict(id="J04", cat="Journal Article", title="A bibliometric insight into immersive technologies for cultural heritage preservation",
         slug="heritage-immersive", img="heritage-immersive.jpg",
         authors="Leilei Jiang, <strong>Jingjing Li</strong>, Walton Wider, Jem Tanucan, et al.",
         venue="<em>npj Heritage Science</em>, 13(1), 2025",
         abstract="This study uses bibliometric analysis to map emerging trends in immersive technologies for cultural heritage preservation. Analyzing Web of Science data through December 2023, it identifies key developments, research gaps, and future directions. Bibliographic coupling and co-word analysis reveal clusters focused on technological applications, digital replication, public engagement, and education. Findings highlight a shift toward interactive preservation methods, offering new insights into how immersive technology is reshaping cultural heritage experiences.",
         cta_label="View on Nature", cta_url="https://doi.org/10.1038/s40494-025-01704-z"),

    dict(id="J05", cat="Journal Article", title="Generative artificial intelligence-guided user studies: an application for air taxi services",
         slug="air-taxi", img="air-taxi.jpg",
         authors="Shengdi Xiao, <strong>Jingjing Li</strong>, Tatsuki Fushimi, Yoichi Ochiai",
         venue="<em>Behaviour &amp; Information Technology</em>, 2025",
         abstract="User studies are crucial for meeting user needs, yet emerging and unfamiliar technologies face limitations including safety concerns and iterative inefficiency. This research employs generative AI to develop synthetic scenarios for evaluating user experience with air taxis — an emerging mobility technology with practical constraints. Language models generated scripts and AI tools produced accompanying visuals; 72 participants then provided feedback on the simulated air taxi journey. Results showed that education level and gender significantly influenced participants' willingness and satisfaction, while contentment mediated openness to the technology. The work demonstrates that generative AI can effectively facilitate user research during the initial design phases of novel, potentially risky applications.",
         cta_label="View on Taylor &amp; Francis", cta_url="https://doi.org/10.1080/0144929X.2025.2462265"),

    dict(id="J06", cat="Journal Article", title="A systematic review of digital transformation technologies in museum exhibition",
         slug="digital-museum-review", img="digital-museum-review.jpg",
         authors="<strong>Jingjing Li</strong>, Xiaoyang Zheng, Ikumu Watanabe, Yoichi Ochiai",
         venue="<em>Computers in Human Behavior</em>, 161, 2024",
         abstract="Museum exhibitions, both temporary and permanent, form an essential link between a society and its cultural, historical, and artistic heritage. Curating artifacts and thematic displays can promote dialogue, foster cultural appreciation, and contribute to heritage preservation. The traditional way of holding museum exhibitions, heavily reliant on the expertise of designers and curatorial staff, makes them a labor-intensive process.\n\nThis review systematically compiles and examines how the application of digital transformation technologies (DTTs) — including artificial intelligence, immersive technologies, additive manufacturing, the Internet of Things, and cloud computing — has revolutionized museum exhibitions and augmented their future potential, helping to create engaging designs, improve accessibility and inclusivity, enhance educational potential, and allow for sophisticated visitor experience data collection.\n\nDespite multiple specialized studies, the roles of DTTs and their connections in exhibition scenarios remain underexplored; addressing this gap, the study informs practitioners and presents new research avenues for scholars.",
         cta_label="View on Elsevier", cta_url="https://doi.org/10.1016/j.chb.2024.108407"),

    dict(id="J07", cat="Journal Article", title="Metaverse chronicles: a bibliometric analysis of its evolving landscape",
         slug="metaverse-chronicles", img="metaverse-chronicles.jpg",
         authors="Walton Wider, Leilei Jiang, Jiaming Lin, Muhammad Ash, <strong>Jingjing Li</strong>, et al.",
         venue="<em>International Journal of Human–Computer Interaction</em>, 2024",
         abstract="The Metaverse — a hypothetical virtual space where people interact with digital environments — has emerged as a significant concept across education, healthcare, and business. While this transformative technology shows considerable promise, a comprehensive understanding of its research landscape and future prospects is essential to guide further exploration. This bibliometric study examined 928 journal articles from the Web of Science database to map current trends and forecast future developments. Through co-citation and co-word analysis, the researchers identified four distinct citation-pattern clusters and five thematic clusters. The findings reveal that, despite the Metaverse's growing relevance to human life, increased scholarly attention remains necessary; the article offers perspectives on the field's current state and trajectory using science mapping methodology.",
         cta_label="View on Taylor &amp; Francis", cta_url="https://doi.org/10.1080/10447318.2023.2227825"),

    dict(id="J08", cat="Journal Article", title="Text-to-Microstructure Generation Using Generative Deep Learning",
         slug="text-microstructure", img="text-microstructure.jpg",
         authors="Xiaoyang Zheng, Ikumu Watanabe, Jamie Paik, <strong>Jingjing Li</strong>, et al.",
         venue="<em>Small</em>, 2024",
         abstract="Designing novel materials depends significantly on understanding design principles, physical mechanisms, and modeling methods of material microstructures, typically requiring experienced designers through multiple trial-and-error rounds. Recent advances in deep generative networks have enabled inverse design, though most studies focus on property-conditional generation of specific structure types, resulting in limited diversity and poor human-computer interaction. This study proposes a pioneering text-to-microstructure generative network (Txt2Microstruct-Net) that enables direct generation of 3D material microstructures from text prompts without additional optimization procedures. The model was trained on a large microstructure-caption paired dataset and is extensible. The network is sufficiently flexible to generate different geometric representations such as voxels and point clouds, and demonstrates strong performance with metamaterials. When integrated with large language models, it offers a user-friendly interactive microstructure design tool with promising potential for material discovery.",
         cta_label="View on Wiley", cta_url="https://doi.org/10.1002/smll.202402685"),

    dict(id="J09", cat="Journal Article", title="Unveiling trends in digital tourism research: A bibliometric analysis of co-citation and co-word analysis",
         slug="digital-tourism", img="digital-tourism.jpg",
         authors="<strong>Jingjing Li</strong>, Walton Wider, Yuzhen Gao, Choon Kit Chan, et al.",
         venue="<em>Environmental and Sustainability Indicators</em>, 2023",
         abstract='Digital tourism has witnessed substantial evolution, shaping the trajectory of research. Employing bibliometric analysis on 1,079 articles from the Web of Science database, this study identifies predominant themes and research trends in digital tourism. Three main co-citation clusters emerged: "Smart tourism destinations and smart tourists," "Evolution and impact of E-tourism on travel behavior," and "Personalized smart experience." Co-word analysis showcased prominent themes such as "AR-Integrated E-Tourism," "Co-creation in smart tourism in China post-COVID-19," and "AI-driven personalized destination recommender systems." The study highlights gaps in research, advocating for socio-cultural preservation alongside technological advancement; co-citation analysis suggests new theoretical directions while AR\'s role in sustainable tourism is spotlighted. Practically, AI and Big Data emerge as pivotal for personalized experiences, with co-word analysis aiding industry foresight and emphasizing AI-driven, sustainable strategies.',
         cta_label="View on Elsevier", cta_url="https://doi.org/10.1016/j.indic.2023.100308"),

    dict(id="J10", cat="Journal Article", title="A bibliometric analysis of immersive technology in museum exhibitions: exploring user experience",
         slug="museum-vr-bibliometric", img="museum-vr-bibliometric.jpg",
         authors="<strong>Jingjing Li</strong>, Walton Wider, Yoichi Ochiai, Muhammad Fauzi, et al.",
         venue="<em>Frontiers in Virtual Reality</em>, 2023",
         abstract="<strong>Introduction.</strong> This study aims to comprehensively understand the existing literature on immersive technology in museum exhibitions, focusing on virtual reality (VR), augmented reality (AR), and the visitor experience. The research utilizes a bibliometric approach by examining a dataset of 722 articles.\n\n<strong>Methods.</strong> The study employs co-citation and co-word analysis to investigate trends and forecast emerging areas, particularly the role of VR in the museum context.\n\n<strong>Results.</strong> The analysis reveals five interconnected thematic clusters: (1) VR and AR-enhanced heritage tourism, (2) VR and AR-enabled virtual museums, (3) interactive digital art education in immersive environments, (4) immersive storytelling in virtual heritage spaces, and (5) mobile AR heritage revival.\n\n<strong>Discussion.</strong> The article highlights influential works and shows the field's emphasis on game-driven experiences and interactive 3D heritage, with VR adoption holding the potential to revolutionize user experiences within the cultural heritage sector.",
         cta_label="View on Frontiers", cta_url="https://doi.org/10.3389/frvir.2023.1240562"),

    dict(id="J11", cat="Journal Article", title="Psychological distance and user engagement in online exhibitions: Visualization of moiré patterns based on electroencephalography signals",
         slug="moire-eeg", img="moire-eeg.jpg",
         authors="<strong>Jingjing Li</strong>, Yang Ye, Zhexin Zhang, Nozomu Yoshida, Xanat Vargas Meza, et al.",
         venue="<em>Frontiers in Psychology</em>, 2022",
         abstract="The COVID-19 pandemic has significantly affected the exhibition of artworks in museums and galleries, and many have moved their collections online. Compared with offline exhibitions, online visitors are often unable to communicate their experience with others. Facilitating communication via Zoom, we established a system that allows two people to visit the museum together through Google Arts and Culture (GA&amp;C). To reduce psychological distance and increase user engagement, we designed a media device based on moiré-pattern visualization of EEG signals. Forty university students were assigned to either the normal online experience (NOEE) group or the EEG signal visualization device (ESVD) group. Independent-samples t-tests showed that ESVD participants perceived a significantly closer psychological distance than NOEE participants (t = −2.699; p = 0.008). A one-way ANOVA showed that participants experienced Task 3 with significantly closer psychological distance than Task 1, 2, and 4. Repeated ANOVAs revealed that the ESVD group reported higher overall engagement with marginal significance (p = 0.056). The study shows that EEG visualization media devices can reduce psychological distance and modestly increase engagement during online exhibitions.",
         cta_label="View on Frontiers", cta_url="https://doi.org/10.3389/fpsyg.2022.954803"),

    # ----- CONFERENCE PAPERS -----
    dict(id="C01", cat="Conference Paper", title="OnomaCompass: A Texture Exploration Interface that Shuttles between Words and Images",
         slug="onomacompass", img="onomacompass.jpg",
         authors="Miki Okamura, Shuhey Koyama, <strong>Jingjing Li</strong>, Yoichi Ochiai",
         venue="<em>Augmented Humans Conference (AHs)</em>, 2026",
         abstract="<em>Abstract not yet publicly available — pending publication of the AHs 2026 proceedings.</em>",
         cta_label="AHs 2026", cta_url="https://www.augmented-humans.org/"),

    dict(id="C02", cat="Conference Paper", title="Visualizing the Electroencephalography Signal Discrepancy When Maintaining Social Distancing: EEG-Based Interactive Moiré Patterns",
         slug="moire-hcii", img="moire-hcii.jpg",
         authors="<strong>Jingjing Li</strong>, Yang Ye, Zhexin Zhang, Yinan Zhao, Xanat Vargas Meza, et al.",
         venue="<em>HCI International 2022 (LNCS 13322)</em>, pp. 185–197, 2022",
         abstract="<em>Abstract not openly indexed by the publisher — please follow the Springer link for the full text.</em>",
         cta_label="View on Springer", cta_url="https://doi.org/10.1007/978-3-031-05900-1_12"),

    dict(id="C03", cat="Conference Paper", title="Transformation of Plants into Polka Dot Arts: Kusama Yayoi as an Inspiration for Deep Learning",
         slug="polkadot", img="polkadot.jpg",
         authors="<strong>Jingjing Li</strong>, Xiaoyang Zheng, Jun Li Lu, Xanat Vargas Meza, et al.",
         venue="<em>HCI International 2022</em>, pp. 270–280, 2022",
         abstract="<em>Abstract not openly indexed by the publisher — please follow the Springer link for the full text.</em>",
         cta_label="View on Springer", cta_url="https://doi.org/10.1007/978-3-031-05028-2_18"),

    dict(id="C04", cat="Conference Paper", title="Electroencephalography and Self-assessment Evaluation of Engagement with Online Exhibitions: Case Study of Google Arts and Culture",
         slug="google-arts", img="google-arts.jpg",
         authors="<strong>Jingjing Li</strong>, Chengbo Sun, Xanat Vargas Meza, Yoichi Ochiai",
         venue="<em>HCI International 2022</em>, pp. 316–331, 2022",
         abstract="<em>Abstract not openly indexed by the publisher — please follow the Springer link for the full text.</em>",
         cta_label="View on Springer", cta_url="https://doi.org/10.1007/978-3-031-05434-1_21"),

    # ----- POSTERS -----
    dict(id="P01", cat="Poster / Extended Abstract", title="Life is Mystery: Reweaving Ordinary Spaces into Fluid Ecologies of Enchantment",
         slug="life-is-mystery", img="life-is-mystery.jpg",
         authors="Shuri Ikeno, Kazuya Izumi, <strong>Jingjing Li</strong>, Tatsuki Fushimi, Yoichi Ochiai",
         venue="<em>CHI Extended Abstracts</em>, 2026",
         abstract='We present Life is Mystery, a design practice for embedding open-ended mysteries into everyday environments to invite sense-making rather than solution seeking. Domestic technologies prioritize convenience and efficiency, often rendering living spaces overly explainable and shrinking room to engage uncertainty. We extend anti-solutionist HCI beyond exhibitions by repositioning "mystery" as a design resource: a physical phenomenon that lacks immediate causal explanation and whose solvability and intent remain unclear. We implement a voice-based LLM brainstorming system that helps creators generate and install context-aligned mysteries in their living spaces. A 14-day in-the-wild study investigates recipients\' sense-making and how LLM supports a shift from solution-oriented thinking to ambiguity.',
         cta_label="View on ACM", cta_url="https://doi.org/10.1145/3772363.3798441"),

    dict(id="P02", cat="Poster", title="Exploring Daily Applications of Wearable Galvanic Vestibular Stimulation via a Self-Customizable Toolkit",
         slug="gvs-toolkit", img="gvs-toolkit.jpg",
         authors="[Author list — to be confirmed], including <strong>Jingjing Li</strong>",
         venue="<em>Augmented Humans Conference (AHs)</em>, 2026",
         abstract="<em>Poster — abstract not yet indexed in open metadata sources. Please contact the author or refer to the AHs 2026 proceedings for the full text.</em>",
         cta_label="AHs 2026", cta_url="https://www.augmented-humans.org/"),

    dict(id="P03", cat="Poster", title="Understanding How International Students Co-develop with AI when Facing Daily Challenges in Japan",
         slug="intl-students-ai", img="intl-students-ai.jpg",
         authors="ChunPi Hsieh, <strong>Jingjing Li</strong>, Ichiro Matsuda, Tatsuki Fushimi, Yoichi Ochiai",
         venue="<em>Augmented Humans Conference (AHs)</em>, 2026",
         abstract="Cultural adaptation challenges pose a significant social issue for international students, affecting academic engagement and well-being. Although AI offers on-demand, multilingual, and conversational support, prior research has largely focused on educational or workplace contexts, leaving its use during study abroad underexplored. To lay an empirical foundation for future AI system design, we examine users' needs and how they co-solve challenges with AI during cultural adaptation. Based on interviews with 20 international students, garbage classification and hair cut were identified as representative challenges. We then conducted a user study (N = 15, international students within six months of arrival), analyzing 154 interaction instances across the two tasks. Task-dependent differences emerged: garbage classification was dominated by rule clarification and information seeking (73.1%), whereas translation (49.2%) and expression support were more prominent in the hair cut. Participants also engaged in multi-turn interactions, treating AI as cognitive collaborators while remaining attentive to limitations related to local rules and personal context. These findings provide empirical evidence of AI use during early-stage cultural adaptation and inform the design of future AI-based support systems, providing a foundation for examining how international students' adaptation practices may co-evolve with AI over time.",
         cta_label="View on ACM", cta_url="https://dl.acm.org/doi/10.1145/3795011.3797370"),

    dict(id="P04", cat="Birds of a Feather", title="Birds of a Feather: Women in CG",
         slug="women-in-cg", img="women-in-cg.jpg",
         authors="Bektur Ryskeldiev, Yuri Mikawa, Maria Larsson, Noshaba Cheema, <strong>Jingjing Li</strong>, Yuka Ikarashi, Shoko Kimura, Miho Aoki, Ayumi Kimura",
         venue="<em>SIGGRAPH Asia 2024</em>, Tokyo, December 2024",
         abstract="Join us for the Women in CG session! The speakers will share their stories and accomplishments, and together we will envision the future of the field — to create a space where every voice is heard and everyone is empowered to make their mark. Together, we can shape the future of the industry.",
         cta_label="View on SIGGRAPH Asia", cta_url="https://asia.siggraph.org/2024/presentation/?id=bof_119&sess=sess238"),

    # ----- PREPRINT -----
    dict(id="X01", cat="Preprint", title="Knowing Ourselves Through Others: Reflecting with AI in Digital Human Debates",
         slug="digital-human-debates", img="digital-human-debates.jpg",
         authors="Ichiro Matsuda, Komichi Takezawa, Katsuhito Muroi, et al. (incl. <strong>Jingjing Li</strong>)",
         venue="<em>arXiv</em>:2511.13046, 2025",
         abstract='LLMs can act as an impartial other, drawing on vast knowledge, or as personalized self-reflecting user prompts. These personalized LLMs, or Digital Humans, occupy an intermediate position between self and other. This research explores the dynamic of self and other mediated by these Digital Humans. Using a Research Through Design approach, nine junior and senior high school students, working in teams, designed Digital Humans and had them debate. Each team built a unique Digital Human using prompt engineering and RAG, then observed their autonomous debates. Findings from generative AI literacy tests, interviews, and log analysis revealed that participants deepened their understanding of AI\'s capabilities. Furthermore, experiencing their own creations as others prompted a reflective attitude, enabling them to objectively view their own cognition and values. We propose "Reflecting with AI" — using AI to re-examine the self — as a new generative AI literacy, complementing the conventional understanding, applying, criticism and ethics.',
         cta_label="View on arXiv", cta_url="https://arxiv.org/abs/2511.13046"),
]

# Group ordering for index
GROUPS = [
    ("Journal Articles", "J"),
    ("International Conference Papers", "C"),
    ("Posters & Presentations", "P"),
    ("Preprints", "X"),
]

# ======================== DETAIL PAGE TEMPLATE ========================
DETAIL_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{TITLE_TXT} — Jingjing Li">
    <title>{TITLE_TXT} — Jingjing Li</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Shippori+Mincho:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <header>
        <nav>
            <a href="../index.html" class="logo">Jingjing Li</a>
            <ul class="nav-links">
                <li><a href="../index.html#about">About</a></li>
                <li><a href="../index.html#research">Research</a></li>
                <li><a href="../index.html#publications">Publications</a></li>
                <li><a href="../index.html#activities">Activities</a></li>
                <li><a href="../index.html#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article class="pub-detail">
            <div class="container narrow">
                <a href="../index.html#publications" class="pub-back">← Back to Publications</a>
                <span class="pub-num">{ID} — {CAT}</span>
                <h1 class="pub-detail-title">{TITLE}</h1>
                <p class="pub-detail-authors">{AUTHORS}</p>
                <p class="pub-detail-venue">{VENUE}</p>
            </div>

            <div class="pub-detail-image-wrap">
                <img src="../images/pubs/{IMG}" alt="{TITLE_TXT}" onerror="this.parentElement.classList.add('no-image')">
            </div>

            <div class="container narrow">
                <h2 class="pub-detail-h2">Abstract</h2>
                <div class="pub-detail-abstract">{ABSTRACT}</div>
                {CTA}
            </div>
        </article>
    </main>

    <footer>
        <p>&copy; 2026 Jingjing Li. Last updated April 2026.</p>
    </footer>

    <script src="../js/script.js"></script>
</body>
</html>
"""

def render_abstract(text):
    """Convert plain abstract (with possible \\n\\n paragraph breaks) into HTML <p> elements."""
    paragraphs = text.split("\n\n")
    return "\n                    ".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())

def render_cta(p):
    if not p["cta_url"]:
        return ""
    return f'<a href="{p["cta_url"]}" target="_blank" rel="noopener" class="pub-cta">{p["cta_label"]} →</a>'

# Strip tags for plain text title
def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)

# ======================== GENERATE DETAIL PAGES ========================
for p in PUBS:
    title_txt = html.escape(strip_tags(p["title"]))
    page = DETAIL_TPL.format(
        TITLE=p["title"],
        TITLE_TXT=title_txt,
        ID=p["id"],
        CAT=p["cat"],
        AUTHORS=p["authors"],
        VENUE=p["venue"],
        IMG=p["img"],
        ABSTRACT=render_abstract(p["abstract"]),
        CTA=render_cta(p),
    )
    fp = os.path.join(OUT_DIR, f"{p['slug']}.html")
    with open(fp, "w") as f:
        f.write(page)
    print(f"  wrote {fp}")

# ======================== GENERATE INDEX LIST SECTION ========================
def render_pub_mini(p):
    return f'''                    <li class="pub-item">
                        <a href="pub/{p["slug"]}.html" class="pub-mini">
                            <div class="pub-mini-thumb"><img src="images/pubs/{p["img"]}" alt="" onerror="this.style.display='none'"></div>
                            <div class="pub-mini-text">
                                <span class="pub-num">{p["id"]}</span>
                                <h4 class="pub-mini-title">{p["title"]}</h4>
                                <span class="pub-mini-authors">{p["authors"]}</span>
                                <span class="pub-mini-venue">{p["venue"]}</span>
                            </div>
                            <span class="pub-mini-arrow" aria-hidden="true">→</span>
                        </a>
                    </li>'''

groups_by_prefix = {prefix: [] for _, prefix in GROUPS}
for p in PUBS:
    prefix = p["id"][0]
    groups_by_prefix[prefix].append(p)

out_lines = []
for label, prefix in GROUPS:
    out_lines.append(f'                <h3 class="pub-cat">{label}</h3>')
    out_lines.append('                <ul class="pub-list">')
    for p in groups_by_prefix[prefix]:
        out_lines.append(render_pub_mini(p))
    out_lines.append('                </ul>')
    out_lines.append('')

with open("/tmp/pubs_section.html", "w") as f:
    f.write("\n".join(out_lines))
print(f"\n  wrote /tmp/pubs_section.html ({len(PUBS)} entries across {len(GROUPS)} groups)")
