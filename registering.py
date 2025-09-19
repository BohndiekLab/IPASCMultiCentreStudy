import SimpleITK as sitk

def coregister(fixed, moving, verbose=1, rigid=True, metric="lstsq"):
    im_fixed = sitk.GetImageFromArray(fixed)
    im_moving = sitk.GetImageFromArray(moving)
    
    if rigid:
        # Setup the registerer
        R = sitk.ImageRegistrationMethod()
        if metric == "lstsq":
            R.SetMetricAsMeanSquares()
        elif metric == "mmi":
            R.SetMetricAsMattesMutualInformation()
        elif metric == "corr":
            R.SetMetricAsCorrelation()
        elif metric == "jhmi":
            R.SetMetricAsJointHistogramMutualInformation()
        elif metric == "ants":
            R.SetMetricAsANTSNeighborhoodCorrelation(radius=20)
        R.SetOptimizerAsRegularStepGradientDescent(1.0, 0.00001, 200)
        R.SetInitialTransform(sitk.TranslationTransform(im_fixed.GetDimension()))
        R.SetInterpolator(sitk.sitkLinear)
    else:
        transformDomainMeshSize = [8] * im_moving.GetDimension()
        tx = sitk.BSplineTransformInitializer(im_fixed, transformDomainMeshSize)

        R = sitk.ImageRegistrationMethod()
        R.SetMetricAsCorrelation()

        R.SetOptimizerAsLBFGSB(
            gradientConvergenceTolerance=1e-5,
            numberOfIterations=100,
            maximumNumberOfCorrections=5,
            maximumNumberOfFunctionEvaluations=1000,
            costFunctionConvergenceFactor=1e7,
        )
        R.SetInitialTransform(tx, True)
        R.SetInterpolator(sitk.sitkLinear)
    
    # if verbose == 2:
    #     R.AddCommand(sitk.sitkIterationEvent, lambda: command_iteration(R))

    outTx = R.Execute(im_fixed, im_moving)
    
    # Setup the resampler
    resampler = sitk.ResampleImageFilter()
    resampler.SetReferenceImage(im_fixed)
    resampler.SetInterpolator(sitk.sitkNearestNeighbor)
    resampler.SetDefaultPixelValue(0)
    resampler.SetTransform(outTx)
    out = resampler.Execute(im_moving)
    
    if verbose == 1:
        print(R.GetOptimizerStopConditionDescription())
    
    return fixed, sitk.GetArrayFromImage(out), resampler
