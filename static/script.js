const txtBox = document.getElementsByClassName('text-box')[0]

function getVar(ele) { // fetches the elements i am looking for, in this case:
    // the image
    // the h1 tag
    // the p tag
    // RIP array programming :/ I miss Python.
    return [ele.childNodes[1], ele.children[1].childNodes[1], ele.children[1].childNodes[3]]
}

function onMouseoverTrigger(ele) {
    

    img = getVar(ele)[0]
    txt = getVar(ele)[1]
    subtext = getVar(ele)[2]

    // Manipulating image
    img.style.transition="1.5s ease";
    img.style.opacity='10%';
    img.style.transform="scale(1.5,1.5)";
    
    //manipulating the header text
    txt.style.transition="1s ease"
    txt.style.textDecoration="underline";
    txt.style.userSelect="none";
    txt.style.transform="translateY(-25vh)";
    
    //manipulating the subtext 
    subtext.style.transform="translateY(-25vh)"
    subtext.style.opacity="1";
    subtext.style.transition="1.5s ease";
    
};

function resetState(ele) {
    
    img = getVar(ele)[0]
    txt = getVar(ele)[1]
    subtext = getVar(ele)[2]
   
    
    // Manipulating image
    img.style.opacity=1;
    img.style.transform="none";
    
    //manipulating the header text
    txt.style.textDecoration="none";
    txt.style.transform="none";
    
    //manipulating the subtext 
    subtext.style.transition="0.5s";
    subtext.style.opacity=0;
    subtext.style.transform="none"
}

function copyToClipboard() {
    const el = document.createElement('textarea');
    el.style.position = 'absolute';
    el.style.left = "-9999px";
    el.innerHTML = 'me@jaes.life'
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    alert('E-mail has been copied to clipboard!')
}

function popUpTextBox() {
    txtBox.style.transition= "all 0.5s ease"
    txtBox.style.opacity=1

}

function removeTextBox() {
    txtBox.style.opacity=0

}





