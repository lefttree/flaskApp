function translate(sourceLang, destLang, sourceId, destId, loadingId) {
    $(destId).hide();
    $(loadingId).show();
    $.post('/translate', {
        text: $(sourceId).text(),
        sourceLang: sourceLang,
        destLang: destLang
    }).done(function(translated){
        $(destId).text(translated['text']);
        $(loadingId).hide();
        $(destId).show();
    }).fail(function(){
        $(destId).text("{{ _('Error: could not contact server.') }}");
        $(loadingId).hide();
        $(destId).show();
    });
}
