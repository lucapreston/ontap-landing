from .pages import Page

UNITS = Page(
    slug="alcohol-units-calculator",
    kind="tool",
    keyword="how many units in a pint",
    title="How Many Units in a Pint? Free Alcohol Units Calculator (UK, US, Canada)",
    h1="How many units are in a pint?",
    description="Free calculator: units in a pint of lager, ale or cider by strength, plus US and Canadian standard drinks. A 4% pint is 2.3 UK units.",
    lede="A pint of 4% lager is <b>2.3 UK units</b>. Pick your drink and strength below to work out units, US standard drinks and Canadian standard drinks for anything you're drinking.",
    publish="2026-10-20",
    body="""
<div class="tool" id="units">
  <div class="row">
    <div><label for="u-size">Drink</label>
      <select id="u-size">
        <option value="568">UK pint (568 ml)</option>
        <option value="284">Half pint (284 ml)</option>
        <option value="473">US pint (16 oz / 473 ml)</option>
        <option value="591">20 oz pint (591 ml)</option>
        <option value="500">500 ml</option>
        <option value="440">Can (440 ml)</option>
        <option value="355">US can or bottle (12 oz / 355 ml)</option>
        <option value="341">Canadian bottle (341 ml)</option>
        <option value="330">Bottle (330 ml)</option>
        <option value="175">Glass of wine (175 ml)</option>
        <option value="25">Single spirit (25 ml)</option>
      </select></div>
    <div><label for="u-abv">Strength (ABV %)</label><input id="u-abv" type="number" step="0.1" min="0" max="70" value="4"></div>
  </div>
  <label for="u-n">How many</label><input id="u-n" type="number" min="1" max="50" value="1">
  <div class="out" id="u-out"></div>
</div>
<script>
(function(){
  var s=document.getElementById('u-size'),a=document.getElementById('u-abv'),n=document.getElementById('u-n'),o=document.getElementById('u-out');
  function f(x){return (Math.round(x*10)/10).toFixed(1);}
  function go(){
    var ml=+s.value, abv=+a.value, k=Math.max(1,+n.value||1);
    var pureMl=ml*abv/100*k;
    var uk=pureMl/10, us=pureMl*0.789/14, ca=pureMl/17.05;
    o.innerHTML='<b>'+f(uk)+'</b> UK units<br>'+f(us)+' US standard drinks · '+f(ca)+' Canadian standard drinks'+
      (uk>14?'<br><small>That\\'s more than the UK guideline of 14 units a week.</small>':'');
  }
  [s,a,n].forEach(function(e){e.addEventListener('input',go);}); go();
})();
</script>
<h2>How to work out units</h2>
<p>One UK unit is 10 ml of pure alcohol. Multiply the strength by the volume in millilitres and divide by 1,000:</p>
<p class="note"><b>Units = ABV (%) × volume (ml) ÷ 1,000</b><br>4% × 568 ml ÷ 1,000 = 2.27, so about <b>2.3 units</b> in a pint of ordinary lager.</p>
<h2>Units in common pints</h2>
<table>
<tr><th>Drink</th><th>Strength</th><th>UK units</th></tr>
<tr><td>Pint of ordinary lager, bitter or cider</td><td>4%</td><td>2.3</td></tr>
<tr><td>Pint of premium lager</td><td>5%</td><td>2.8</td></tr>
<tr><td>Pint of strong lager or cider</td><td>5.5%</td><td>3.1</td></tr>
<tr><td>Pint of stout</td><td>4.2%</td><td>2.4</td></tr>
<tr><td>Pint of IPA</td><td>6%</td><td>3.4</td></tr>
<tr><td>Half pint of 4% lager</td><td>4%</td><td>1.1</td></tr>
<tr><td>440 ml can of 5% lager</td><td>5%</td><td>2.2</td></tr>
</table>
<h2>Units vs standard drinks</h2>
<p>Countries count differently. The UK uses <b>units</b> (8 g of alcohol). The US counts <b>standard drinks</b> of about 14 g, like a 12 oz can of 5% beer. Canada's standard drink is 13.45 g (17.05 ml), like a 341 ml bottle of 5% beer. That's why a UK pint of 4% lager is 2.3 units but only about 1.3 US standard drinks.</p>
<h2>How much is too much?</h2>
<p>The UK Chief Medical Officers advise not regularly drinking more than <b>14 units a week</b>, spread over three or more days, with some drink-free days. That's about six pints of 4% lager a week. If you want to keep an eye on it, a free tracker like <a href="https://www.drinkaware.co.uk/tools/mydrinkaware-app" rel="nofollow noopener">MyDrinkaware</a> is built for exactly that.</p>
""",
    faq=[
        ("How many units are in a pint of Guinness?", "Guinness Draught is 4.2% in the UK, so a pint is about 2.4 units (4.2 × 568 ÷ 1,000)."),
        ("How many units in a pint of 5% lager?", "About 2.8 units: 5 × 568 ÷ 1,000 = 2.84."),
        ("Is a US pint the same as a UK pint?", "No. A UK pint is 568 ml (20 imperial fl oz); a US pint is 473 ml (16 US fl oz), about 17% smaller."),
        ("How long does a unit take to leave your body?", "Roughly an hour per unit for most adults, but it varies a lot from person to person, and nothing speeds it up. Never drive after drinking."),
    ],
    related=["price-per-pint-calculator", "round-splitter", "best-drink-tracker-apps"],
)

PRICE = Page(
    slug="price-per-pint-calculator",
    kind="tool",
    keyword="price per pint calculator",
    title="Price Per Pint Calculator: Compare Pints, Cans and Pitchers",
    h1="Price per pint calculator",
    description="Is the pitcher, the 20 oz or the can the better deal? Compare up to three drinks by price per UK pint, US pint and per 100 ml.",
    lede="Bars sell beer in all sorts of sizes. Put in the price and size of up to three options and see which is actually cheapest per pint.",
    publish="2026-10-20",
    body="""
<div class="tool" id="ppp">
  <div id="ppp-rows"></div>
  <label for="ppp-cur">Currency</label>
  <select id="ppp-cur"><option>£</option><option>$</option><option>€</option></select>
  <div class="out" id="ppp-out"></div>
</div>
<script>
(function(){
  var sizes=[["568","UK pint (568 ml)"],["473","US pint (16 oz)"],["591","20 oz"],["284","Half pint"],["500","500 ml"],["440","Can (440 ml)"],["330","Bottle (330 ml)"],["1420","Pitcher (2.5 pints)"],["1893","Pitcher (64 oz)"]];
  var defs=[[6.5,"568"],[22,"1420"],[2.4,"440"]];
  var box=document.getElementById('ppp-rows'),cur=document.getElementById('ppp-cur'),o=document.getElementById('ppp-out');
  defs.forEach(function(d,i){
    var opts=sizes.map(function(s){return '<option value="'+s[0]+'"'+(s[0]===d[1]?' selected':'')+'>'+s[1]+'</option>';}).join('');
    box.insertAdjacentHTML('beforeend','<div class="row"><div><label>Option '+(i+1)+' price</label><input type="number" step="0.01" min="0" value="'+d[0]+'" data-p></div><div><label>Size</label><select data-s>'+opts+'</select></div></div>');
  });
  function go(){
    var ps=box.querySelectorAll('[data-p]'),ss=box.querySelectorAll('[data-s]'),c=cur.value,best=-1,bestV=1e9,lines=[];
    for(var i=0;i<ps.length;i++){
      var p=+ps[i].value, ml=+ss[i].value; if(!p||!ml){lines.push('');continue;}
      var uk=p/ml*568; if(uk<bestV){bestV=uk;best=i;}
      lines.push('Option '+(i+1)+': '+c+uk.toFixed(2)+' per UK pint · '+c+(p/ml*473).toFixed(2)+' per US pint · '+c+(p/ml*100).toFixed(2)+' per 100 ml');
    }
    o.innerHTML=(best>=0?'<b>Option '+(best+1)+' is cheapest</b><br>':'')+lines.filter(Boolean).join('<br>');
  }
  box.addEventListener('input',go); cur.addEventListener('input',go); go();
})();
</script>
<h2>Why sizes are confusing</h2>
<p>A "pint" isn't the same everywhere. In the UK and Ireland it's 568 ml by law. In the US it's 16 oz (473 ml), and plenty of American bars pour 14 oz glasses and still call them pints. In Canada you'll see 16 oz, 20 oz (568 ml) and 500 ml all called a pint or a <i>pinte</i>. Comparing on price per pint, or per 100 ml, is the only fair way.</p>
<h2>Quick rules of thumb</h2>
<ul>
<li>A pitcher is only a deal if you'd finish it at the same pace; flat, warm beer isn't a bargain.</li>
<li>Happy hour on a 16 oz pour can still cost more per pint than full price on a 20 oz.</li>
<li>Cans from the shop are almost always cheapest per pint, which is why pubs are a treat.</li>
</ul>
<p>Want real numbers? See what a pint actually costs in <a href="/price-of-a-pint-in-london/">London</a>, <a href="/price-of-a-pint-in-new-york/">New York</a>, <a href="/price-of-a-pint-in-montreal/">Montréal</a> and <a href="/price-of-a-pint-in-toronto/">Toronto</a>.</p>
""",
    faq=[
        ("How many ml is a pint?", "568 ml in the UK and Ireland (20 imperial fl oz); 473 ml in the US (16 US fl oz)."),
        ("How many pints in a pitcher?", "A UK pitcher is usually 2.5 pints (about 1.4 litres). A US pitcher is commonly 60–64 oz, roughly 3.75–4 US pints."),
        ("How many pints in a 440 ml can?", "About 0.77 of a UK pint, or 0.93 of a US pint."),
    ],
    related=["alcohol-units-calculator", "round-splitter", "price-of-a-pint-in-london"],
)

ROUNDS = Page(
    slug="round-splitter",
    kind="tool",
    keyword="split the bar tab calculator",
    title="Round Splitter: Who Owes What After a Night of Rounds",
    h1="Round splitter: who owes what?",
    description="Free calculator to settle up after a night of rounds. Add who bought each round and how much, and it tells you who owes whom.",
    lede="Somebody always ends up buying one round too many. Add the rounds below and settle up fairly in seconds.",
    publish="2026-10-20",
    body="""
<div class="tool" id="rs">
  <label for="rs-names">Who was out? (comma separated)</label>
  <input id="rs-names" value="Sam, Alex, Jordan, Priya">
  <div id="rs-rounds"></div>
  <button type="button" id="rs-add">+ Add a round</button>
  <div class="out" id="rs-out"></div>
</div>
<script>
(function(){
  var names=document.getElementById('rs-names'),box=document.getElementById('rs-rounds'),o=document.getElementById('rs-out');
  function people(){return names.value.split(',').map(function(s){return s.trim();}).filter(Boolean);}
  function opts(sel){return people().map(function(p){return '<option'+(p===sel?' selected':'')+'>'+p.replace(/</g,'')+'</option>';}).join('');}
  function add(who,amt){box.insertAdjacentHTML('beforeend','<div class="row"><div><label>Paid by</label><select data-w>'+opts(who)+'</select></div><div><label>Amount</label><input type="number" step="0.01" min="0" value="'+amt+'" data-a></div></div>');}
  function refresh(){box.querySelectorAll('[data-w]').forEach(function(s){var v=s.value;s.innerHTML=opts(v);});go();}
  function go(){
    var ps=people(); if(ps.length<2){o.textContent='Add at least two people.';return;}
    var paid={},total=0; ps.forEach(function(p){paid[p]=0;});
    var ws=box.querySelectorAll('[data-w]'),as=box.querySelectorAll('[data-a]');
    for(var i=0;i<ws.length;i++){var a=+as[i].value||0; if(paid[ws[i].value]!==undefined){paid[ws[i].value]+=a;total+=a;}}
    var share=total/ps.length,bal=ps.map(function(p){return [p,paid[p]-share];});
    var debt=bal.filter(function(b){return b[1]<-0.005;}).map(function(b){return [b[0],-b[1]];});
    var cred=bal.filter(function(b){return b[1]>0.005;});
    var out=[],i=0,j=0;
    while(i<debt.length&&j<cred.length){var x=Math.min(debt[i][1],cred[j][1]);out.push(debt[i][0]+' pays '+cred[j][0]+' <b>'+x.toFixed(2)+'</b>');debt[i][1]-=x;cred[j][1]-=x;if(debt[i][1]<0.005)i++;if(cred[j][1]<0.005)j++;}
    o.innerHTML='Total '+total.toFixed(2)+' · '+share.toFixed(2)+' each<br>'+(out.length?out.join('<br>'):'Everyone\\'s square. 🍻');
  }
  document.getElementById('rs-add').addEventListener('click',function(){add(people()[0],0);go();});
  names.addEventListener('change',refresh); box.addEventListener('input',go);
  add('Sam',24); add('Alex',22.5); add('Sam',26); go();
})();
</script>
<h2>How it works</h2>
<p>It adds up everything that was spent, splits it evenly between everyone who was out, then works out the fewest payments to settle up. If someone skipped a round on purpose (driving, slow drinker, left early), just leave them out of the list.</p>
<h2>Round etiquette, briefly</h2>
<ul>
<li>Big group? Split into smaller rounds or a kitty. Six rounds of six is a lot of rounds.</li>
<li>It's fine to sit out a round. A soft drink round counts too.</li>
<li>Settle up the same night or the next morning, while everyone remembers.</li>
</ul>
<p>ontap can't split the bill, but it does remember who was out and where, which helps when the debate starts.</p>
""",
    faq=[
        ("What if someone only had soft drinks?", "Leave them out of the list and settle their share separately, or add their own round so it balances."),
        ("Does it work with any currency?", "Yes. It's just numbers; use whatever currency you paid in."),
    ],
    related=["price-per-pint-calculator", "alcohol-units-calculator", "best-social-apps-for-nights-out"],
)

ABV = Page(
    slug="abv-calculator",
    kind="tool",
    keyword="beer abv calculator",
    title="Beer ABV Calculator: Original and Final Gravity to ABV",
    h1="Beer ABV calculator",
    description="Homebrew ABV calculator: enter original and final gravity to get alcohol by volume, apparent attenuation and the units in a pint of your beer.",
    lede="Brewing at home? Enter your original gravity (OG) and final gravity (FG) to get the strength of your beer.",
    publish="2026-10-20",
    body="""
<div class="tool" id="abv">
  <div class="row">
    <div><label for="og">Original gravity (OG)</label><input id="og" type="number" step="0.001" value="1.050"></div>
    <div><label for="fg">Final gravity (FG)</label><input id="fg" type="number" step="0.001" value="1.010"></div>
  </div>
  <div class="out" id="abv-out"></div>
</div>
<script>
(function(){
  var og=document.getElementById('og'),fg=document.getElementById('fg'),o=document.getElementById('abv-out');
  function go(){
    var a=+og.value,b=+fg.value; if(!a||!b||a<=b){o.textContent='OG needs to be higher than FG.';return;}
    var simple=(a-b)*131.25;
    var alt=(76.08*(a-b)/(1.775-a))*(b/0.794);
    var att=(a-b)/(a-1)*100;
    o.innerHTML='<b>'+simple.toFixed(1)+'% ABV</b><br>Advanced formula: '+alt.toFixed(1)+'% · Attenuation: '+att.toFixed(0)+'%<br>A UK pint of it: '+(simple*568/1000).toFixed(1)+' units';
  }
  [og,fg].forEach(function(e){e.addEventListener('input',go);}); go();
})();
</script>
<h2>The formula</h2>
<p class="note"><b>ABV ≈ (OG − FG) × 131.25</b><br>(1.050 − 1.010) × 131.25 = 5.25% ABV.</p>
<p>That simple formula is accurate for most beers up to about 7–8%. For big beers (barley wines, imperial stouts) the "advanced" formula above is closer, because the relationship between sugar and alcohol stops being linear.</p>
<h2>Tips for a reliable reading</h2>
<ul>
<li>Take readings at the temperature your hydrometer is calibrated for (often 20 °C / 68 °F), or correct for it.</li>
<li>Wait until FG is stable for two or three days before bottling.</li>
<li>Refractometers read differently once there's alcohol in the beer; use a correction calculator for FG.</li>
</ul>
""",
    faq=[
        ("What's a normal original gravity?", "Most everyday ales and lagers start around 1.040–1.055. Stronger IPAs and stouts often start at 1.060–1.080 or more."),
        ("What does attenuation mean?", "How much of the sugar the yeast ate. 70–80% apparent attenuation is typical for ales."),
    ],
    related=["alcohol-units-calculator", "best-beer-apps", "best-apps-for-craft-beer-lovers"],
)

PAGES = [UNITS, PRICE, ROUNDS, ABV]
