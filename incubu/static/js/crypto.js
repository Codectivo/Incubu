var Incubu = {
    key: null,
    iv: CryptoJS.lib.WordArray.random(16)
};

// var encrypted = CryptoJS.AES.encrypt("Holitaaa", Incubu.key, {iv: Incubu.iv});
// var decrypted = CryptoJS.AES.decrypt(encrypted, Incubu.key, {iv: Incubu.iv});
//console.log(encrypted + "-----" + decrypted.toString(CryptoJS.enc.Utf8));

function encrypt_str(str){
    if(Incubu.key){
        var encrypted = CryptoJS.AES.encrypt(str, Incubu.key, {iv: Incubu.iv});
        return encrypted.toString();
    }else{
        return false;
    }
}

function decrypt_str(str){
    if(Incubu.key){
        var decrypted = CryptoJS.AES.decrypt(str, Incubu.key, {iv: Incubu.iv});
        return decrypted.toString(CryptoJS.enc.Utf8)
    }else{
        return false;
    }
}
