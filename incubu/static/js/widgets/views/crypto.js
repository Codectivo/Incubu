define(['backbone', 'underscore', 'aes'], function (BB, _) {
    var Incubu = {
            key: null,
            iv: CryptoJS.lib.WordArray.random(16)
    };
    return BB.View.extend({

        initialize: function(){
        },

        render: function(){
            // var encrypted = CryptoJS.AES.encrypt("Holitaaa", Incubu.key, {iv: Incubu.iv});
            // var decrypted = CryptoJS.AES.decrypt(encrypted, Incubu.key, {iv: Incubu.iv});
            //console.log(encrypted + "-----" + decrypted.toString(CryptoJS.enc.Utf8));
        },

        getIncubu: function(){
            return Incubu;
        },

        encrypt_str: function(str){
                if(Incubu.key){
                    var encrypted = CryptoJS.AES.encrypt(str, Incubu.key, {iv: Incubu.iv});
                    return encrypted.toString();
                }else{
                    return false;
                }
        },

        decrypt_str: function(str){
                if(Incubu.key){
                    var decrypted = CryptoJS.AES.decrypt(str, Incubu.key, {iv: Incubu.iv});
                    return decrypted.toString(CryptoJS.enc.Utf8)
                }else{
                    return false;
                }
        },

        set_key: function(str){
            if(str){
                Incubu.key = str;
                return true;
            }else{
                return false;
            }
        },

        get_key: function(){
            return Incubu.key ? true: false;
        }
    });
});
