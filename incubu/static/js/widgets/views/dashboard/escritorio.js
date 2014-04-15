define(['backbone', 'jquery', 'widgets/views/crypto', 'aes'], function (BB, $, CryptoF) {
    return BB.View.extend({
        el: $("#escritorio"),

        initialize: function () {
            this.render();
        },

        render: function(){
            var view=this,
                cryptof = new CryptoF({});;

            $("#link_desktop").click(function(){
                $("#table_keys").fadeIn();
                $("#add_key").hide();
            });

            $("#link_add_clave").click(function(){
                $("#table_keys").hide();
                $("#add_key").fadeIn();
            });

            $("#submit_add_clave").click(function(){
                if(cryptof.get_key){
                    var err_ms = "Ocurrio un error, estamos trabajando para resolverlo",
                        response = "",
                        description = $("#id_description").val(),
                        user = $("#id_user_account").val(),
                        pass = $("#id_pass_account").val(),
                        data_send = {
                            'description': cryptof.encrypt_str(description),
                            'user_account': cryptof.encrypt_str(user),
                            'pass_account': cryptof.encrypt_str(pass),
                            'csrfmiddlewaretoken':  $.cookie("csrftoken")
                        };
                    if($("#submit_add_clave").attr('data-type') == 'add'){
                        if(user && pass && description){
                            $.ajax({
                                async: false,
                                type: "POST",
                                url: "/usuario/add_key/",
                                data: data_send,
                                success: function(response){
                                    response = $.parseJSON(response);
                                    if(response.estatus === true){
                                        $("#table_keys").fadeIn();
                                        $("#add_key").hide();
                                        $("#table_keys tbody").append("<tr><td>"+description
                                            +"</td><td>"+user+"</td><td>"
                                            +pass
                                            +"<td></td><td></td>");
                                    }else{
                                        alert(err_ms);
                                    }
                                },
                                error: function(requestData, strError, strTipoError){
                                    alert(err_ms);
                                }
                            });
                        }else{
                            alert("Asegurate de llenar todos los campos");
                        }
                    }else{
                        // Edit
                        data_send['account_id'] = $("#submit_add_clave").attr("data-edit-id");
                        if(user && pass && description){
                            $.ajax({
                                async: false,
                                type: "POST",
                                url: "/usuario/edit_key/",
                                data: data_send,
                                success: function(response){
                                    response = $.parseJSON(response);
                                    if(response.estatus === true){
                                        $("#table_keys").fadeIn();
                                        $("#add_key").hide();
                                        $("." + data_send['account_id']+" td:eq(0)").html(description);
                                        $("." + data_send['account_id']+" td:eq(1)").html(user);
                                        $("." + data_send['account_id']+" td:eq(2)").html(pass);
                                    }else{
                                        alert(err_ms);
                                    }
                                },
                                error: function(requestData, strError, strTipoError){
                                    alert(err_ms);
                                }
                            });
                        }else{
                            alert("Asegurate de llenar todos los campos");
                        }
                    }
                }else{
                    alert("Antes de guardar la cuenta debes introducir un Frase para encriptar tus cuentas.");
                    $("#id_key").focus();
                }
            });

            $("#load_key").click(function(){
                if($("#id_key").val()!=""){
                    var description = null,
                        user = null,
                        pass = null,
                        dec_description = null,
                        dec_user = null,
                        dec_pass = null,
                        dec_tru = true;
                    cryptof.set_key($("#id_key").val());
                    $('#accounts > tbody  > tr').each(function(){
                        description = $('td:eq(0)', $(this)).attr('data');
                        user = $('td:eq(1)', $(this)).attr('data');
                        pass = $('td:eq(2)', $(this)).attr('data');
                        dec_description = cryptof.decrypt_str(description);
                        dec_user = cryptof.decrypt_str(user);
                        dec_pass = cryptof.decrypt_str(pass);
                        if(dec_description != "" && dec_user != "" && dec_pass != ""){
                            $('td:eq(0)', $(this)).html(dec_description);
                            $('td:eq(1)', $(this)).html(dec_user);
                            $('td:eq(2)', $(this)).html(dec_pass);
                            $('td:eq(3)', $(this)).find(".edit_account").css({'display': 'block'});
                            $('td:eq(4)', $(this)).find(".delete_account").css({'display': 'block'});
                        }else{
                            dec_tru = false;
                        }
                    });
                    if(dec_tru){
                        $("#init_clave").html("<p>Frase cargada correctamente.</p>");
                    }else{
                        alert("Frase incorrecta, imposible desencriptar.");
                        cryptof.set_key(null);
                        $("#id_key").val(null);
                        $("#id_key").focus();
                    }
                }else{
                    alert("Debes introducir una frase.");
                }
            });

            $(".delete_account").click(function(){
                if(cryptof.get_key){
                    var view = $(this),
                        err_ms = "Ocurrio un error, estamos trabajando para resolverlo",
                        data_send = {
                        'data_id': view.attr('data'),
                        'csrfmiddlewaretoken':  $.cookie("csrftoken")
                        };
                    if(confirm("Estas seguro de eliminar esta cuenta?")){
                        $.ajax({
                            async: false,
                            type: "POST",
                            url: "/usuario/delete_key/",
                            data: data_send,
                            success: function(response){
                                response = $.parseJSON(response);
                                if(response.estatus === true){
                                    view.parents("tr").fadeOut("normal");
                                }
                                else{
                                    alert(err_ms);
                                }
                            },
                            error: function(requestData, strError, strTipoError){
                                alert(err_ms);
                            }
                        });
                    }
                }else{
                    alert("Debes introducir una frase.");
                }
            });

            $(".edit_account").click(function(){
                if(cryptof.get_key){
                    var view = $(this),
                        description = cryptof.decrypt_str(view.attr('data-description')),
                        user = cryptof.decrypt_str(view.attr('data-user')),
                        pass = cryptof.decrypt_str(view.attr('data-pass'));
                    $("#table_keys").hide();
                    $("#add_key").fadeIn();
                    $("#id_description").val(description);
                    $("#id_user_account").val(user);
                    $("#id_pass_account").val(pass);
                    $("#submit_add_clave").attr({'data-type': 'edit', 'data-edit-id': view.attr('data-acc-id')});
                }else{
                    alert("Debes introducir una frase.");
                }
            });
        }
    });
});
