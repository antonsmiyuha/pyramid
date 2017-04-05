<div class="row">
    %for message in request.session.pop_flash():
        <span class="col-12 alert alert-danger">
            ${ message }
        </span>
    %endfor
</div>