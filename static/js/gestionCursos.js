//------TYPE SCRIPT--------------
(function () {
    
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) =>{

            const confirmacion=confirm("¿Estas seguro de Eliminar el Curso ?");

            if(!confirmacion){
                e.preventDefault();
            }

        });
    });
})();