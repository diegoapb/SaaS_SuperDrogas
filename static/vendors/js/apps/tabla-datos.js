//script que permite generar una tabla de datos con la información traducida
$.fn.dataTableExt.ofnSearch['string'] = function (data) {
    return !data ?
        '' :
        typeof data === 'string' ?
            data
                .replace(/\n/g, ' ')
                .replace(/á/g, 'a')
                .replace(/é/g, 'e')
                .replace(/í/g, 'i')
                .replace(/ó/g, 'o')
                .replace(/ú/g, 'u')
                .replace(/ê/g, 'e')
                .replace(/î/g, 'i')
                .replace(/ô/g, 'o')
                .replace(/è/g, 'e')
                .replace(/ï/g, 'i')
                .replace(/ü/g, 'u')
                .replace(/ç/g, 'c')
                .replace(/Á/g, 'A')
                .replace(/É/g, 'E')
                .replace(/Í/g, 'I')
                .replace(/Ó/g, 'O')
                .replace(/Ú/g, 'U')
            :
            data;
};

if ($('.data-combine').length !== 0) {
    function existe_columnas() {
        return function (idx, data, node) {
            var columna = $('.data-combine').DataTable().column(idx);
            var titulo_encabezado = $(node).html();
            var imprimir_columna = columna.visible();
            if (titulo_encabezado === "Opciones" || titulo_encabezado === "Acciones") {
                imprimir_columna = false
            }
            return imprimir_columna;
        };
    }

    $('.data-combine').DataTable({
        dom: 'lBfrtip',
        columnDefs: [
            {searchable: false, targets: ['no-search']},
            {orderable: false, targets: ['no-order']},
            {visible: false, targets: ['hide-default']},
        ],
        buttons: [
            {
                extend: 'copy',
                className: 'btn-sm',
                text: 'Copiar',
                exportOptions: {
                    columns: existe_columnas()
                }
            },
            {
                extend: 'csv',
                className: 'btn-sm',
                exportOptions: {
                    columns: existe_columnas()
                }
            },
            {
                extend: 'excel',
                className: 'btn-sm',
                exportOptions: {
                    columns: existe_columnas()
                }
            },
            {
                extend: 'pdf',
                className: 'btn-sm',
                exportOptions: {
                    columns: existe_columnas()
                }
            },
            {
                extend: 'print',
                className: 'btn-sm',
                text: 'Imprimir',
                exportOptions: {
                    columns: existe_columnas()
                }
            },
            {
                extend: 'colvis',
                className: 'btn-sm',
                text: 'Mostrar/Ocultar columnas'
            }
        ],
        "language": {
            "processing": "Procesando...",
            "lengthMenu": "Mostrar _MENU_ registros",
            "zeroRecords": "No se encontraron resultados",
            "emptyTable": "Ningún dato disponible en esta tabla",
            "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "infoFiltered": "(filtrado de un total de _MAX_ registros)",
            "search": "Buscar:",
            "decimal": "",
            "infoPostFix": "",
            "thousands": ",",
            "loadingRecords": "Cargando...",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sortDescending": ": Activar para ordenar la columna de manera descendente"
            },
            buttons: {
                copyTitle: 'Copiado a portapapeles',
                copySuccess: {
                    _: '%d lineas copiadas',
                    1: '1 linea copiada'
                }
            }
        },
        "order": [],
        colReorder: true,
        keys: true,
        rowReorder: false,
        select: true
    });
}
